# yuki documentation

* Project README: [English](../src/README.md) · [Русский](../src/README.ru.md)
* Security model and threat list: [`src/DESIGN.md`](../src/DESIGN.md) (Russian)
* Building your own index, step by step: [`src/TUTORIAL.md`](../src/TUTORIAL.md) (Russian)
* Language roadmap: [`roadmap.md`](roadmap.md)

## Language reference — [`lang/en`](lang/en) · [`lang/ru`](lang/ru)

Every page exists in English and Russian; the switcher sits under the title.

| Page | English | Русский |
|---|---|---|
| Yukino Documentation | [0-overview.md](lang/en/0-overview.md) | [0-overview.md](lang/ru/0-overview.md) |
| Installing Yukino | [1-setup.md](lang/en/1-setup.md) | [1-setup.md](lang/ru/1-setup.md) |
| Macro System and Built-in Macros | [10-macros.md](lang/en/10-macros.md) | [10-macros.md](lang/ru/10-macros.md) |
| System C ABI and C FFI | [11-cabi.md](lang/en/11-cabi.md) | [11-cabi.md](lang/ru/11-cabi.md) |
| Core Library: core | [12-core-library.md](lang/en/12-core-library.md) | [12-core-library.md](lang/ru/12-core-library.md) |
| Compiler Attributes | [13-attributes.md](lang/en/13-attributes.md) | [13-attributes.md](lang/ru/13-attributes.md) |
| Error Handling and Exceptions (sus, catch, finally, panic) | [14-errors.md](lang/en/14-errors.md) | [14-errors.md](lang/ru/14-errors.md) |
| Workspaces and Multi-Package Projects (yukispace.toml) | [15-workspaces.md](lang/en/15-workspaces.md) | [15-workspaces.md](lang/ru/15-workspaces.md) |
| 16. Testing and Test Runner | [16-tests.md](lang/en/16-tests.md) | [16-tests.md](lang/ru/16-tests.md) |
| Toolchain and Project Structure | [2-cli-project.md](lang/en/2-cli-project.md) | [2-cli-project.md](lang/ru/2-cli-project.md) |
| Basic Syntax, Operators, and Control Flow | [3-basics.md](lang/en/3-basics.md) | [3-basics.md](lang/ru/3-basics.md) |
| Type System and Pattern Matching | [4-types.md](lang/en/4-types.md) | [4-types.md](lang/ru/4-types.md) |
| Functions and Closures | [5-functions-closures.md](lang/en/5-functions-closures.md) | [5-functions-closures.md](lang/ru/5-functions-closures.md) |
| Memory Model, Ownership, and Regions | [6-memory.md](lang/en/6-memory.md) | [6-memory.md](lang/ru/6-memory.md) |
| Structures, Classes, and Interfaces | [7-oop.md](lang/en/7-oop.md) | [7-oop.md](lang/ru/7-oop.md) |
| Strings and Bytes | [8-strings.md](lang/en/8-strings.md) | [8-strings.md](lang/ru/8-strings.md) |
| Modules, Imports, and the Visibility System | [9-modules.md](lang/en/9-modules.md) | [9-modules.md](lang/ru/9-modules.md) |
| Editor Extensions and Yukino LSP | [extensions.md](lang/en/extensions.md) | [extensions.md](lang/ru/extensions.md) |

## Standard library — [`lang/en/stdlib`](lang/en/stdlib) · [`lang/ru/stdlib`](lang/ru/stdlib)

| Module | English | Русский |
|---|---|---|
| Standard Library (stdlib): Overview | [0-overview.md](lang/en/stdlib/0-overview.md) | [0-overview.md](lang/ru/stdlib/0-overview.md) |
| Module std.strings | [1-strings.md](lang/en/stdlib/1-strings.md) | [1-strings.md](lang/ru/stdlib/1-strings.md) |
| Module std.process | [10-process.md](lang/en/stdlib/10-process.md) | [10-process.md](lang/ru/stdlib/10-process.md) |
| Module std.os | [11-os.md](lang/en/stdlib/11-os.md) | [11-os.md](lang/ru/stdlib/11-os.md) |
| Module std.sysinfo | [12-sysinfo.md](lang/en/stdlib/12-sysinfo.md) | [12-sysinfo.md](lang/ru/stdlib/12-sysinfo.md) |
| Module std.env | [13-env.md](lang/en/stdlib/13-env.md) | [13-env.md](lang/ru/stdlib/13-env.md) |
| Module std.simpleurl | [14-simpleurl.md](lang/en/stdlib/14-simpleurl.md) | [14-simpleurl.md](lang/ru/stdlib/14-simpleurl.md) |
| Module std.compress | [15-compress.md](lang/en/stdlib/15-compress.md) | [15-compress.md](lang/ru/stdlib/15-compress.md) |
| Module std.fs.archives | [16-archives.md](lang/en/stdlib/16-archives.md) | [16-archives.md](lang/ru/stdlib/16-archives.md) |
| Module std.locale | [17-locale.md](lang/en/stdlib/17-locale.md) | [17-locale.md](lang/ru/stdlib/17-locale.md) |
| Module std.numf | [18-numf.md](lang/en/stdlib/18-numf.md) | [18-numf.md](lang/ru/stdlib/18-numf.md) |
| Module std.sharedc | [19-sharedc.md](lang/en/stdlib/19-sharedc.md) | [19-sharedc.md](lang/ru/stdlib/19-sharedc.md) |
| Module std.io | [2-io.md](lang/en/stdlib/2-io.md) | [2-io.md](lang/ru/stdlib/2-io.md) |
| Module std.json | [20-json.md](lang/en/stdlib/20-json.md) | [20-json.md](lang/ru/stdlib/20-json.md) |
| Module std.jsonc | [21-jsonc.md](lang/en/stdlib/21-jsonc.md) | [21-jsonc.md](lang/ru/stdlib/21-jsonc.md) |
| Module std.outf | [22-outf.md](lang/en/stdlib/22-outf.md) | [22-outf.md](lang/ru/stdlib/22-outf.md) |
| Module std.line | [23-line.md](lang/en/stdlib/23-line.md) | [23-line.md](lang/ru/stdlib/23-line.md) |
| Module std.itermtool | [24-itermtool.md](lang/en/stdlib/24-itermtool.md) | [24-itermtool.md](lang/ru/stdlib/24-itermtool.md) |
| Module std.stdotool | [25-stdotool.md](lang/en/stdlib/25-stdotool.md) | [25-stdotool.md](lang/ru/stdlib/25-stdotool.md) |
| Module std.hash | [26-hash.md](lang/en/stdlib/26-hash.md) | [26-hash.md](lang/ru/stdlib/26-hash.md) |
| Module std.crypto | [27-crypto.md](lang/en/stdlib/27-crypto.md) | [27-crypto.md](lang/ru/stdlib/27-crypto.md) |
| Module std.net | [28-net.md](lang/en/stdlib/28-net.md) | [28-net.md](lang/ru/stdlib/28-net.md) |
| Module std.regex | [29-regex.md](lang/en/stdlib/29-regex.md) | [29-regex.md](lang/ru/stdlib/29-regex.md) |
| Module std.threads | [3-threads.md](lang/en/stdlib/3-threads.md) | [3-threads.md](lang/ru/stdlib/3-threads.md) |
| Module std.toml | [30-toml.md](lang/en/stdlib/30-toml.md) | [30-toml.md](lang/ru/stdlib/30-toml.md) |
| Module std.yaml | [31-yaml.md](lang/en/stdlib/31-yaml.md) | [31-yaml.md](lang/ru/stdlib/31-yaml.md) |
| Module std.sqlite | [32-sqlite.md](lang/en/stdlib/32-sqlite.md) | [32-sqlite.md](lang/ru/stdlib/32-sqlite.md) |
| Module std.encore | [33-encore.md](lang/en/stdlib/33-encore.md) | [33-encore.md](lang/ru/stdlib/33-encore.md) |
| Module std.platformio | [4-platformio.md](lang/en/stdlib/4-platformio.md) | [4-platformio.md](lang/ru/stdlib/4-platformio.md) |
| Module std.math | [5-math.md](lang/en/stdlib/5-math.md) | [5-math.md](lang/ru/stdlib/5-math.md) |
| Module std.datetime | [6-datetime.md](lang/en/stdlib/6-datetime.md) | [6-datetime.md](lang/ru/stdlib/6-datetime.md) |
| Module std.random | [7-random.md](lang/en/stdlib/7-random.md) | [7-random.md](lang/ru/stdlib/7-random.md) |
| Module std.fs | [8-fs.md](lang/en/stdlib/8-fs.md) | [8-fs.md](lang/ru/stdlib/8-fs.md) |
| Module std.collections | [9-collections.md](lang/en/stdlib/9-collections.md) | [9-collections.md](lang/ru/stdlib/9-collections.md) |

## Toolchain internals — [`dev`](dev)

Notes on the compiler, build pipeline and project layout (Russian).

## LLM context — [`LLM`](LLM)

Agent-oriented reference for the Yukino language: [`LLM/SKILL.md`](LLM/SKILL.md) and the
compact topic references in [`LLM/references/en`](LLM/references/en), including the
`build.ykn` pre-build script contract in
[`2-cli-project.md`](LLM/references/en/2-cli-project.md).
