#!/usr/bin/env python3
"""
Generate Async*Client.pyi stub files and AsyncClient.pyi from the sync sources.

Runtime behaviour is fully dynamic: AsyncClient uses the sync resource clients
unchanged, and its async _get/_post/_patch/_delete dispatch methods make every
call awaitable.  These .pyi stubs exist solely for static type checkers — they
declare every resource method as `async def` with the correct return type.

Usage:
    python scripts/generate_async_stubs.py          # generate all
    python scripts/generate_async_stubs.py --check  # verify up-to-date (CI)
"""

import ast
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RESOURCES_DIR = REPO_ROOT / "paddle_billing" / "Resources"
ASYNC_CLIENT_PY = REPO_ROOT / "paddle_billing" / "AsyncClient.py"

STUB_HEADER = """\
# AUTO-GENERATED STUB — DO NOT EDIT DIRECTLY.
# Source: {source_rel}
# Regenerate with: python scripts/generate_async_stubs.py
#
# This is a type-checker-only (.pyi) stub file. It is NOT importable at runtime.
# Import AsyncClient from paddle_billing.AsyncClient; do not import this file directly.
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _find_class(tree: ast.Module) -> ast.ClassDef | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            return node
    return None


def _imports_section(source: str) -> str:
    """Return every line before the first top-level `class` statement."""
    lines = source.splitlines(keepends=True)
    result = []
    for line in lines:
        if re.match(r"^class ", line):
            break
        result.append(line)
    return "".join(result).rstrip("\n")


def _fix_client_import(content: str) -> str:
    return content.replace(
        "from paddle_billing.Client import Client",
        "from paddle_billing.AsyncClient import AsyncClient",
    )


def _func_stub(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    *,
    force_async: bool | None = None,
    indent: int = 4,
) -> str:
    """Return a single-line stub for a function/method."""
    pad = " " * indent

    is_async = isinstance(node, ast.AsyncFunctionDef) if force_async is None else force_async

    decorator_lines = [f"{pad}@{ast.unparse(d)}" for d in node.decorator_list]

    args = ast.unparse(node.args)
    # __init__ in resource clients uses client: 'Client' — fix for the stub
    args = re.sub(r"client: 'Client'", "client: 'AsyncClient'", args)

    ret = f" -> {ast.unparse(node.returns)}" if node.returns else ""
    # __init__ always returns None
    if node.name == "__init__" and not node.returns:
        ret = " -> None"

    kw = "async def" if is_async else "def"
    sig = f"{pad}{kw} {node.name}({args}){ret}: ..."

    return "\n".join(decorator_lines + [sig])


# ---------------------------------------------------------------------------
# Resource client stubs  →  Async*Client.pyi
# ---------------------------------------------------------------------------

def generate_resource_stub(source: str, source_rel: str) -> str:
    tree = ast.parse(source)
    class_node = _find_class(tree)
    if not class_node:
        raise ValueError(f"No class found in {source_rel}")

    async_name = f"Async{class_node.name}"
    imports = _fix_client_import(_imports_section(source))

    class_lines = [f"\n\nclass {async_name}:"]
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            class_lines.append(_func_stub(node, force_async=(node.name != "__init__")))

    return STUB_HEADER.format(source_rel=source_rel) + imports + "\n".join(class_lines) + "\n"


# ---------------------------------------------------------------------------
# AsyncClient stub  →  AsyncClient.pyi
# ---------------------------------------------------------------------------

def _resource_attrs_from_init(init_node: ast.FunctionDef) -> dict[str, str]:
    """
    Walk __init__ and collect  self.attr = SomeSyncClient(self)  assignments.
    Returns {attr_name: SyncClientClassName}.
    """
    attrs: dict[str, str] = {}
    for stmt in ast.walk(init_node):
        if not (
            isinstance(stmt, ast.Assign)
            and len(stmt.targets) == 1
            and isinstance(stmt.targets[0], ast.Attribute)
            and isinstance(stmt.targets[0].value, ast.Name)
            and stmt.targets[0].value.id == "self"
            and isinstance(stmt.value, ast.Call)
            and isinstance(stmt.value.func, ast.Name)
            and stmt.value.func.id.endswith("Client")
            and stmt.value.func.id != "AsyncClient"
        ):
            continue
        attrs[stmt.targets[0].attr] = stmt.value.func.id
    return attrs


def generate_async_client_stub(source: str) -> str:
    tree = ast.parse(source)

    class_node = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "AsyncClient":
            class_node = node
            break
    if not class_node:
        raise ValueError("AsyncClient class not found")

    # Find the __init__ node to extract resource attributes
    init_node = next(
        (n for n in class_node.body if isinstance(n, ast.FunctionDef) and n.name == "__init__"),
        None,
    )
    resource_attrs = _resource_attrs_from_init(init_node) if init_node else {}

    # Replace sync resource-client imports with Async* variants
    imports = _imports_section(source)
    for cls in set(resource_attrs.values()):
        imports = re.sub(
            rf"from (paddle_billing\.Resources\.[^.]+\.){re.escape(cls)} import {re.escape(cls)}",
            rf"from \g<1>Async{cls} import Async{cls}",
            imports,
        )

    class_lines = ["\n\nclass AsyncClient:"]
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            if node.name == "__init__":
                class_lines.append(_func_stub(node, force_async=False))
                # Declare all resource attributes right after __init__
                for attr, cls in sorted(resource_attrs.items()):
                    class_lines.append(f"    {attr}: Async{cls}")
            else:
                class_lines.append(_func_stub(node, force_async=False))
        elif isinstance(node, ast.AsyncFunctionDef):
            class_lines.append(_func_stub(node, force_async=True))

    return STUB_HEADER.format(source_rel="paddle_billing/AsyncClient.py") + imports + "\n".join(class_lines) + "\n"


# ---------------------------------------------------------------------------
# File discovery and I/O
# ---------------------------------------------------------------------------

def find_sync_clients() -> list[Path]:
    return sorted(
        p for p in RESOURCES_DIR.rglob("*Client.py")
        if not p.name.startswith("Async")
    )


def stub_path(sync_path: Path) -> Path:
    return sync_path.with_name(f"Async{sync_path.stem}.pyi")


def main() -> int:
    check_mode = "--check" in sys.argv
    failures: list[Path] = []

    targets: list[tuple[Path, str]] = []

    for sync_path in find_sync_clients():
        source = sync_path.read_text()
        source_rel = str(sync_path.relative_to(REPO_ROOT))
        generated = generate_resource_stub(source, source_rel)
        out = stub_path(sync_path)
        targets.append((out, generated))

    # AsyncClient.pyi
    async_client_pyi = ASYNC_CLIENT_PY.with_suffix(".pyi")
    async_client_stub = generate_async_client_stub(ASYNC_CLIENT_PY.read_text())
    targets.append((async_client_pyi, async_client_stub))

    for out, content in targets:
        if check_mode:
            if not out.exists() or out.read_text() != content:
                print(f"OUT OF DATE: {out.relative_to(REPO_ROOT)}")
                failures.append(out)
        else:
            out.write_text(content)
            print(f"Generated: {out.relative_to(REPO_ROOT)}")

    if check_mode:
        if failures:
            print(f"\n{len(failures)} file(s) out of date. Run: python scripts/generate_async_stubs.py")
            return 1
        print("All async stub files are up to date.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
