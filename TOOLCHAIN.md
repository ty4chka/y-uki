# Yukino toolchain

Yuki is written in Yukino; the compiler and language server are maintained upstream.

- Compiler and CLI: [yukitsuri/yukino](https://github.com/yukitsuri/yukino), release `v0.1.1`.
- LSP: [yukitsuri/yukino-lsp](https://github.com/yukitsuri/yukino-lsp), release `0.1.1`.
- Source repositories are included as Git submodules in `toolchain/`.
- Use the upstream release binaries for your platform; do not place the 154 MB compiler binary in Git history.

Clone with submodules:

```sh
git clone --recurse-submodules https://github.com/ty4chka/y-uki.git
```

Linux x86_64 GNU downloads:

```sh
mkdir -p bin
curl -fL https://github.com/yukitsuri/yukino/releases/download/v0.1.1/yukic-linux-gnu-x86_64 -o bin/yukic
curl -fL https://github.com/yukitsuri/yukino-lsp/releases/download/0.1.1/yukino-lsp-linux-gnu-x86_64 -o bin/yukino-lsp
chmod +x bin/yukic bin/yukino-lsp
```
