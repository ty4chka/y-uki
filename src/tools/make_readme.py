import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Labeled artwork lives in assets/en/ and assets/ru/ (see make_assets.py);
# language-neutral pieces (num-, who-, sec-, divider, palette, preview) are shared.
LABELED = {"banner", "btn-start", "btn-tutorial", "btn-security", "btn-commands",
           "status", "stat-cmds", "stat-errors", "stat-servers", "stat-modes",
           "card-signed", "card-priv", "card-fast", "card-tx", "card-build", "card-graph"}

def pic(lang, name, alt, width=None, link=None):
    base = f"assets/{lang}" if name in LABELED else "assets"
    w = f' width="{width}"' if width else ""
    img = (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}/{name}-dark.svg">'
           f'<img alt="{alt}" src="{base}/{name}-light.svg"{w}></picture>')
    return f'<a href="{link}">{img}</a>' if link else img

def icon(name, h=34):
    return f'<img src="assets/sec-{name}.svg" height="{h}" align="absmiddle" alt="">'

def step(lang, n, title, body, who=None):
    chip = f'<img src="assets/who-{who}.svg" height="28" alt="{who}">' if who else ""
    return (f'<tr><td width="96" valign="top"><img src="assets/num-{n}.svg" width="72" alt="{n}"></td>'
            f'<td valign="top"><b>{title}</b><br>{body}</td><td valign="top" align="right">{chip}</td></tr>')

S = {
"en": {
 "switch": '<p align="center"><b>English</b> · <a href="README.ru.md">Русский</a></p>',
 "banner_alt": "yuki: package manager for Yukino",
 "tagline": "<sub>The package manager for Yukino. No servers of your own, with signatures and rollback.</sub>",
 "btn_start_alt": "Quick start", "btn_tut_alt": "Your own index: tutorial",
 "btn_sec_alt": "Security model", "btn_cmd_alt": "All commands",
 "status_alt": "status: builds and passes selftest",
 "stat_cmds_alt": "commands", "stat_errors_alt": "explained errors",
 "stat_servers_alt": "servers of your own", "stat_modes_alt": "terminal modes",
 "about_h": "What it is",
 "about_p1": """**yuki** installs applications system-wide (`sudo yuki install`, like pacman) and libraries into
projects (`yuki add`, written to `yuki.toml`).""",
 "about_p2": """The registry is an ordinary git repository: GitHub serves the files and trust comes from signatures
and hashes, so **no servers of your own are needed**.""",
 "gif_alt": "install with a growing dependency tree",
 "gif_cap": "Live panel: phases on top, the dependency tree grows below, downloads run in parallel",
 "card_signed_alt": "Signed index", "card_priv_alt": "No root until the end",
 "card_fast_alt": "Parallel downloads", "card_tx_alt": "Transactions and rollback",
 "card_build_alt": "No binary? We build it", "card_graph_alt": "Package links",
 "start_h": "Quick start",
 "step1_t": "Build and verify", "step1_b": "the first build compiles the sources; <code>selftest</code> then checks hashes, signatures and threads against known values",
 "step2_t": "Point at an index and a trusted key", "step2_b": "the key fingerprint is shown and asked to be confirmed",
 "step3_t": "Use it", "step3_b": "pacman-style flags work",
 "how_h": "How an install runs",
 "how_p": "Root appears only where the system must change, and it trusts nothing at face value.",
 "how1_t": "The child brings index records", "how1_b": "<code>fork</code>, drop root, <code>no_new_privs</code>",
 "how2_t": "Root re-verifies and builds the plan", "how2_b": "signature, expiry, rollback, key roles, content confirmation, the \"continue?\" question",
 "how3_t": "Parallel download and build", "how3_b": "thread pool, hashing in the worker; app builds run in bubblewrap without network and the result is checked against the signed hash",
 "how4_t": "Root copies to itself and checks files", "how4_b": "BLAKE3, archive audit, path policy, safe symlinks, nobody processes killed",
 "how5_t": "A transaction with a journal", "how5_b": "journal and backups hit the disk before the first change, auto-rollback after a crash",
 "cmds_h": "Commands",
 "cmds_p": "<code>yuki help &lt;command&gt;</code> gives examples, <code>yuki explain Y0301</code> explains any error, and typos get a suggestion.",
 "cmds_th1": "System (<code>sudo</code>)", "cmds_th2": "Look around", "cmds_th3": "Projects and service",
 "flags": "Flags like in pacman",
 "pac_th": ["pacman", "yuki", "pacman", "yuki"],
 "pac_rows": [
   ["`-S pkg`", "install", "`-Q`", "list"],
   ["`-Syu`", "upgrade everything", "`-Qi pkg`", "info"],
   ["`-Ss word`", "search", "`-Ql pkg`", "files"],
   ["`-Si pkg`", "description", "`-Qo path`", "owns"],
   ["`-R pkg`", "remove", "`-Qe` / `-Qd`", "explicit / dependencies"],
   ["`-Rs pkg`", "with unneeded dependencies", "`-Qdt`", "orphans"],
   ["`-Sc` / `-Scc`", "clean the cache", "`-Qu` / `-Qk`", "outdated / check files"],
 ],
 "sec_h": "Security",
 "sec_th": ["Threat", "What stops it"],
 "sec_rows": [
   ["Swapped archive or index", "BLAKE3 + Ed25519, re-verified as root"],
   ["Rollback and a frozen index", "`seq`, `expires`, local `seen` state"],
   ["Leaked renewal key", "the `renewer` role cannot sign release content"],
   ["Leaked publisher key", "publisher threshold (`publish_threshold`), `cosign`, rotation and revocation"],
   ["Malicious archive", "audit before unpack, path policy, symlink checks, size limits"],
   ["Network or build compromise", "privilege separation, bubblewrap, signed result hash"],
   ["Power loss mid-install", "journal on disk, auto-rollback on the next run"],
 ],
 "sec_more": "The full story, including **what is not protected**, is in [`DESIGN.md`](DESIGN.md) (Russian).",
 "look_h": "How it looks",
 "look_cap1": "<code>sudo yuki install</code>",
 "look_cap2": "every error carries <code>help</code> and a <code>yuki explain</code> link",
 "look_cap3": "One result in three modes: truecolor, your terminal colors (<code>palette = \"ansi\"</code>) and ASCII",
 "look_p": """A single theme, tunable through `theme.toml`: colors, symbols, animation. Everything degrades on
its own: truecolor → 256 → 16 → no color, UTF-8 → ASCII, a live terminal → a plain log for CI. `NO_COLOR=1` works.""",
 "look_note": "> The pictures illustrate what the code does rather than real runs. Package names, hashes and numbers in them are invented.",
 "theme_path": "~/.config/yuki/theme.toml  or  /etc/yuki/theme.toml",
 "theme_palette": '"rgb" | "ansi" (terminal colors) | "mono"',
 "index_h": "Your own index in an evening",
 "idx1_t": "Repository", "idx1_b": "copy <code>yuki-index-template/</code>, turn on branch protection for <code>main</code> and CODEOWNERS",
 "idx2_t": "Keys", "idx2_b": "<code>yuki keys gen main</code>, the public part into <code>keys/trusted_keys</code>, the secret stays offline",
 "idx3_t": "Package", "idx3_b": "<code>yuki pack</code> builds the archive and runs the policy checks, the release is published on GitHub",
 "idx4_t": "Record", "idx4_b": "<code>yuki index add release.json main</code> downloads, verifies and signs; a second publisher runs <code>cosign</code>",
 "idx5_t": "CI", "idx5_b": "<code>yuki index check download</code> on every PR and monthly key renewal with the <code>renewer</code> key",
 "idx_more": "Step by step: [`TUTORIAL.md`](TUTORIAL.md) (Russian). Repository template: [`yuki-index-template/`](yuki-index-template/).",
 "faq_h": "FAQ",
 "faq": [
  ("Do I need my own servers?", "No. The index lives in a git repository, the client fetches files over HTTPS (you can list several mirrors) and verifies the signatures itself."),
  ("Why is system installation only via sudo?", "Installing changes the system. Networking and building run without privileges, root re-verifies everything and applies a single journaled transaction."),
  ("What if there is no prebuilt binary?", "For applications yuki either installs a signed prebuilt binary or builds from source: the build runs in bubblewrap (no network, read-only root, only the build directory writable), and the build command, the file list and the signed result hash are shown and require your consent. In scripts the flag is <code>--allow-build</code>. Without bubblewrap the build is refused until the admin explicitly allows unsandboxed builds."),
  ("How do libraries differ?", "A <code>kind = \"lib\"</code> entry is source-only: no prebuilt library artifacts are accepted anywhere, and libraries use the C FFI. If the source archive contains a <code>build.ykn</code> script, its contents are displayed and it runs only after explicit confirmation. Library builds skip the heavy app sandbox and network rules."),
  ("How does yuki update itself?", "<code>sudo yuki self-update</code>. The new binary must be able to start, otherwise the update rolls back."),
  ("A key leaked. What now?", "Sign a <code>rotation.json</code> revoking it with enough keys and run <code>sudo yuki keys refresh</code>. A revoked key never comes back."),
  ("Does this work?", "Yes, as verified: both source trees compile with the Yukino toolchain, <code>yuki selftest</code> passes (hashing, signing, verification, threads, files) and the language server reports no diagnostics on the sources. What the security model deliberately does not cover is listed in <code>DESIGN.md</code>."),
 ],
 "footer": '<p align="center"><sub>yuki · for <a href="https://github.com/yukitsuri/yukino">Yukino</a> · <a href="TUTORIAL.md">tutorial</a> · <a href="DESIGN.md">security model</a> (Russian)</sub></p>',
 "use_block": """```bash
yuki -Ss grep                  # search
yuki -Si ripgrep               # description
sudo yuki -S ripgrep pcre2     # install, one plan and one transaction
sudo yuki -Syu                 # upgrade everything, also one transaction
sudo yuki -Rs ripgrep          # remove with unneeded dependencies
yuki related ripgrep           # what is linked to what
sudo yuki rollback             # undo the last transaction
```""",
 "key_block": """```bash
sudo mkdir -p /etc/yuki
echo https://raw.githubusercontent.com/YOU/yuki-index/main | sudo tee /etc/yuki/index_url
sudo yuki keys trust main <public-key>
```""",
},
"ru": {
 "switch": '<p align="center"><a href="README.md">English</a> · <b>Русский</b></p>',
 "banner_alt": "yuki: менеджер пакетов для Yukino",
 "tagline": "<sub>The package manager for Yukino. No servers, with signatures and rollback.</sub>",
 "btn_start_alt": "Быстрый старт", "btn_tut_alt": "Свой индекс: туториал",
 "btn_sec_alt": "Модель защиты", "btn_cmd_alt": "Все команды",
 "status_alt": "статус: сборка проходит, selftest зелёный",
 "stat_cmds_alt": "команд", "stat_errors_alt": "ошибок с разбором",
 "stat_servers_alt": "своих серверов", "stat_modes_alt": "режима терминала",
 "about_h": "Что это",
 "about_p1": """**yuki** ставит приложения в систему (`sudo yuki install`, как pacman) и библиотеки в проекты
(`yuki add`, запись в `yuki.toml`).""",
 "about_p2": """Реестр это обычный git-репозиторий: файлы раздаёт GitHub, а доверие строится на подписях
и хешах, поэтому **свои серверы не нужны**.""",
 "gif_alt": "установка с растущим деревом зависимостей",
 "gif_cap": "Живая панель: фазы сверху, дерево зависимостей растёт снизу, загрузки идут параллельно",
 "card_signed_alt": "Подписанный индекс", "card_priv_alt": "Без root до конца",
 "card_fast_alt": "Параллельные загрузки", "card_tx_alt": "Транзакции и откат",
 "card_build_alt": "Нет бинарника? Соберём", "card_graph_alt": "Связи пакетов",
 "start_h": "Быстрый старт",
 "step1_t": "Соберите и проверьте сборку", "step1_b": "первая сборка компилирует исходники, затем <code>selftest</code> сверит хеши, подписи и потоки с эталонами",
 "step2_t": "Укажите индекс и доверенный ключ", "step2_b": "отпечаток ключа покажут и попросят подтвердить",
 "step3_t": "Пользуйтесь", "step3_b": "флаги как у pacman работают",
 "how_h": "Как проходит установка",
 "how_p": "Root появляется только там, где нужно менять систему, и ничему не верит на слово.",
 "how1_t": "Ребёнок приносит записи индекса", "how1_b": "<code>fork</code>, отказ от root, <code>no_new_privs</code>",
 "how2_t": "Root заново проверяет и строит план", "how2_b": "подпись, срок, откат, роли ключей, подтверждение содержимого, вопрос «продолжить?»",
 "how3_t": "Параллельное скачивание и сборка", "how3_b": "пул потоков, хеш считается в воркере; сборка приложений в bubblewrap без сети, результат сверяется с подписанным хешем",
 "how4_t": "Root копирует к себе и проверяет файлы", "how4_b": "BLAKE3, аудит архива, политика путей, безопасные симлинки, процессы nobody убиты",
 "how5_t": "Транзакция с журналом", "how5_b": "журнал и резервные копии на диск до первого изменения, автооткат после сбоя",
 "cmds_h": "Команды",
 "cmds_p": "<code>yuki help &lt;команда&gt;</code> даёт примеры, <code>yuki explain Y0301</code> объясняет любую ошибку, при опечатке подсказывает правильную команду.",
 "cmds_th1": "Система (<code>sudo</code>)", "cmds_th2": "Посмотреть", "cmds_th3": "Проекты и сервис",
 "flags": "Флаги как в pacman",
 "pac_th": ["pacman", "yuki", "pacman", "yuki"],
 "pac_rows": [
   ["`-S pkg`", "установить", "`-Q`", "список"],
   ["`-Syu`", "обновить всё", "`-Qi pkg`", "info"],
   ["`-Ss слово`", "поиск", "`-Ql pkg`", "files"],
   ["`-Si pkg`", "описание", "`-Qo путь`", "owns"],
   ["`-R pkg`", "удалить", "`-Qe` / `-Qd`", "явные / зависимости"],
   ["`-Rs pkg`", "с ненужными зависимостями", "`-Qdt`", "сироты"],
   ["`-Sc` / `-Scc`", "очистить кэш", "`-Qu` / `-Qk`", "устаревшие / проверка файлов"],
 ],
 "sec_h": "Защита",
 "sec_th": ["Угроза", "Чем закрыта"],
 "sec_rows": [
   ["Подмена архива или индекса", "BLAKE3 + Ed25519, повторная проверка в root"],
   ["Откат и «замороженный» индекс", "`seq`, `expires`, локальное состояние `seen`"],
   ["Утёкший ключ автопродления", "роль `renewer` не может подписать содержимое релизов"],
   ["Утёкший ключ издателя", "порог издателей (`publish_threshold`), `cosign`, ротация и отзыв"],
   ["Вредный архив", "аудит до распаковки, политика путей, проверка симлинков, лимиты"],
   ["Компрометация сети или сборки", "разделение привилегий, bubblewrap, подписанный хеш результата"],
   ["Сбой питания посреди установки", "журнал на диск, автооткат при следующем запуске"],
 ],
 "sec_more": "Подробно и **что не защищено** описано в [`DESIGN.md`](DESIGN.md).",
 "look_h": "Как выглядит",
 "look_cap1": "<code>sudo yuki install</code>",
 "look_cap2": "ошибка всегда с <code>help</code> и ссылкой на <code>yuki explain</code>",
 "look_cap3": "Один результат в трёх режимах: truecolor, цвета вашего терминала (<code>palette = \"ansi\"</code>) и ASCII",
 "look_p": """Одна тема, настраиваемая файлом `theme.toml`: цвета, символы, анимация. Всё подстраивается само:
truecolor → 256 → 16 → без цвета, UTF-8 → ASCII, живой терминал → простой лог для CI. `NO_COLOR=1` работает.""",
 "look_note": "> Картинки показывают логику кода, а не снимки реального запуска. Названия пакетов, хеши и цифры в них выдуманы.",
 "theme_path": "~/.config/yuki/theme.toml  или  /etc/yuki/theme.toml",
 "theme_palette": '"rgb" | "ansi" (цвета терминала) | "mono"',
 "index_h": "Свой индекс за вечер",
 "idx1_t": "Репозиторий", "idx1_b": "скопируйте <code>yuki-index-template/</code>, включите защиту ветки <code>main</code> и CODEOWNERS",
 "idx2_t": "Ключи", "idx2_b": "<code>yuki keys gen main</code>, публичную часть в <code>keys/trusted_keys</code>, секрет офлайн",
 "idx3_t": "Пакет", "idx3_b": "<code>yuki pack</code> собирает архив и проверяет политику, релиз выкладывается на GitHub",
 "idx4_t": "Запись", "idx4_b": "<code>yuki index add релиз.json main</code> скачает, проверит и подпишет; второй издатель делает <code>cosign</code>",
 "idx5_t": "CI", "idx5_b": "<code>yuki index check download</code> на каждый PR и ежемесячное продление ключом <code>renewer</code>",
 "idx_more": "Пошагово: [`TUTORIAL.md`](TUTORIAL.md). Шаблон репозитория: [`yuki-index-template/`](yuki-index-template/).",
 "faq_h": "FAQ",
 "faq": [
  ("Нужны ли мне свои серверы?", "Нет. Индекс лежит в git-репозитории, клиент берёт файлы по HTTPS (можно указать несколько зеркал) и сам проверяет подписи."),
  ("Почему установка только через sudo?", "Установка меняет систему. Но сеть и сборка выполняются без прав, а root проверяет всё заново и применяет одну транзакцию с журналом."),
  ("Что, если нет готового бинарника?", "Для приложений yuki ставит подписанный бинарник или собирает из исходников: сборка идёт в bubblewrap (без сети, корень только для чтения, писать можно только в каталог сборки), а команда сборки, список файлов и подписанный хеш результата показываются и требуют согласия. В скриптах флаг <code>--allow-build</code>. Без bubblewrap сборка отклоняется, пока админ явно не разрешил сборку без песочницы."),
  ("Чем библиотеки отличаются?", "Запись <code>kind = \"lib\"</code> — только исходники: готовые бинарные артефакты для библиотек не принимаются нигде, а связь с кодом идёт через C FFI. Если в архиве исходников есть <code>build.ykn</code>, его содержимое показывается и выполняется только после явного подтверждения. Сборка библиотек не использует тяжёлую песочницу приложений и сетевые правила."),
  ("Как обновляется сам yuki?", "<code>sudo yuki self-update</code>. Новый бинарник обязан запуститься, иначе обновление откатывается."),
  ("Утёк ключ. Что делать?", "Подписать <code>rotation.json</code> с отзывом нужным числом ключей и выполнить <code>sudo yuki keys refresh</code>. Отозванный ключ больше не вернётся."),
  ("Это уже работает?", "Да, в проверенном объёме: оба дерева исходников компилируются тулчейном Yukino, <code>yuki selftest</code> проходит (хеши, подписи, проверки, потоки, файлы), языковой сервер не находит диагностики в исходниках. Что модель защиты сознательно не покрывает — перечислено в <code>DESIGN.md</code>."),
 ],
 "footer": '<p align="center"><sub>yuki · для <a href="https://github.com/yukitsuri/yukino">Yukino</a> · <a href="TUTORIAL.md">туториал</a> · <a href="DESIGN.md">модель защиты</a></sub></p>',
 "use_block": """```bash
yuki -Ss grep                  # поиск
yuki -Si ripgrep               # описание
sudo yuki -S ripgrep pcre2     # установка, одним планом и одной транзакцией
sudo yuki -Syu                 # обновить всё, тоже одной транзакцией
sudo yuki -Rs ripgrep          # удалить вместе с ненужными зависимостями
yuki related ripgrep           # что с чем связано
sudo yuki rollback             # отменить последнюю транзакцию
```""",
 "key_block": """```bash
sudo mkdir -p /etc/yuki
echo https://raw.githubusercontent.com/YOU/yuki-index/main | sudo tee /etc/yuki/index_url
sudo yuki keys trust main <публичный-ключ>
```""",
},
}

BUILD_BLOCK = """```bash
cd yuki && yukino build release
sudo install -m 755 yuki-work/local/build/release/*/yuki/yuki /usr/local/bin/yuki
yuki selftest && yuki doctor
```"""

def theme_block(t):
    return f"""```toml
# {t["theme_path"]}
palette = "ansi"            # {t["theme_palette"]}

[colors]
accent = "ansi:cyan"
bad    = "#f38ba8+bold"

[style]
animation = true
bar_gradient = true
```"""

CMDS = {
 "sys": "`install` `reinstall`<br>\n`uninstall [-s]` `autoremove`<br>\n`upgrade` `self-update`<br>\n`hold` `unhold`<br>\n`rollback` `history`",
 "view": "`search` `show`<br>\n`list` `info` `files` `owns`<br>\n`why` `tree` `rdeps` `related`<br>\n`graph [dot]` `orphans`<br>\n`outdated` `check` `sys-audit`",
 "proj": "`add` `remove` `update`<br>\n`fetch` `audit`<br>\n`keys` `theme` `pack`<br>\n`index add|cosign|check|catalog`<br>\n`doctor` `config` `clean` `selftest`",
}

def render(lang):
    t = S[lang]
    md = []
    md.append(f'''{t["switch"]}

<div align="center">

{pic(lang, "banner", t["banner_alt"], 880)}

{t["tagline"]}

<p>
{pic(lang, "btn-start", t["btn_start_alt"], 230, "#start")}
{pic(lang, "btn-tutorial", t["btn_tut_alt"], 280, "TUTORIAL.md")}
</p>
<p>
{pic(lang, "btn-security", t["btn_sec_alt"], 230, "DESIGN.md")}
{pic(lang, "btn-commands", t["btn_cmd_alt"], 200, "#commands")}
</p>

{pic(lang, "status", t["status_alt"])}

<p>
{pic(lang, "stat-cmds", t["stat_cmds_alt"], 205)}
{pic(lang, "stat-errors", t["stat_errors_alt"], 205)}
{pic(lang, "stat-servers", t["stat_servers_alt"], 205)}
{pic(lang, "stat-modes", t["stat_modes_alt"], 205)}
</p>

</div>

{pic(lang, "divider", "", 880)}
''')

    md.append(f'''<a name="about"></a>
## {icon("arrow")} {t["about_h"]}

{t["about_p1"]}
{t["about_p2"]}

<p align="center"><img src="assets/preview/yuki-live.gif" width="760" alt="{t["gif_alt"]}"></p>
<p align="center"><sub>{t["gif_cap"]}</sub></p>

<table align="center">
<tr>
<td>{pic(lang, "card-signed", t["card_signed_alt"], 290)}</td>
<td>{pic(lang, "card-priv", t["card_priv_alt"], 290)}</td>
<td>{pic(lang, "card-fast", t["card_fast_alt"], 290)}</td>
</tr>
<tr>
<td>{pic(lang, "card-tx", t["card_tx_alt"], 290)}</td>
<td>{pic(lang, "card-build", t["card_build_alt"], 290)}</td>
<td>{pic(lang, "card-graph", t["card_graph_alt"], 290)}</td>
</tr>
</table>
''')

    md.append(f'''<a name="start"></a>
## {icon("arrow")} {t["start_h"]}

<table>
{step(lang, 1, t["step1_t"], t["step1_b"])}
</table>

{BUILD_BLOCK}

<table>
{step(lang, 2, t["step2_t"], t["step2_b"])}
</table>

{t["key_block"]}

<table>
{step(lang, 3, t["step3_t"], t["step3_b"])}
</table>

{t["use_block"]}
''')

    md.append(f'''<a name="how"></a>
## {icon("priv")} {t["how_h"]}

{t["how_p"]}

<table>
{step(lang, 1, t["how1_t"], t["how1_b"], "nobody")}
{step(lang, 2, t["how2_t"], t["how2_b"], "root")}
{step(lang, 3, t["how3_t"], t["how3_b"], "nobody")}
{step(lang, 4, t["how4_t"], t["how4_b"], "root")}
{step(lang, 5, t["how5_t"], t["how5_b"], "root")}
</table>
''')

    pac_rows = "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in t["pac_rows"])
    md.append(f'''<a name="commands"></a>
## {icon("grid")} {t["cmds_h"]}

{t["cmds_p"]}

<table>
<tr><th align="left">{t["cmds_th1"]}</th><th align="left">{t["cmds_th2"]}</th><th align="left">{t["cmds_th3"]}</th></tr>
<tr valign="top"><td>

{CMDS["sys"]}

</td><td>

{CMDS["view"]}

</td><td>

{CMDS["proj"]}

</td></tr>
</table>

<details><summary><b>{t["flags"]}</b></summary>

| {t["pac_th"][0]} | {t["pac_th"][1]} | {t["pac_th"][2]} | {t["pac_th"][3]} |
|---|---|---|---|
{pac_rows}

</details>
''')

    sec_rows = "\n".join(f"| {a} | {b} |" for a, b in t["sec_rows"])
    md.append(f'''<a name="security"></a>
## {icon("sign")} {t["sec_h"]}

| {t["sec_th"][0]} | {t["sec_th"][1]} |
|---|---|
{sec_rows}

{t["sec_more"]}
''')

    md.append(f'''<a name="look"></a>
## {icon("palette")} {t["look_h"]}

<table>
<tr>
<td><img src="assets/preview/yuki-sys-install.png" alt="{t["look_cap1"]}"></td>
<td><img src="assets/preview/yuki-sys-errors.png" alt="{t["look_cap2"]}"></td>
</tr>
<tr>
<td align="center"><sub>{t["look_cap1"]}</sub></td>
<td align="center"><sub>{t["look_cap2"]}</sub></td>
</tr>
</table>

<p align="center"><img src="assets/preview/yuki-modes.png" width="520" alt="{t["look_cap3"]}"></p>
<p align="center"><sub>{t["look_cap3"]}</sub></p>

{t["look_p"]}

<p align="center"><img src="assets/palette.svg" width="560" alt="theme palette"></p>

{theme_block(t)}

{t["look_note"]}
''')

    md.append(f'''<a name="index"></a>
## {icon("graph")} {t["index_h"]}

<table>
{step(lang, 1, t["idx1_t"], t["idx1_b"])}
{step(lang, 2, t["idx2_t"], t["idx2_b"])}
{step(lang, 3, t["idx3_t"], t["idx3_b"])}
{step(lang, 4, t["idx4_t"], t["idx4_b"])}
{step(lang, 5, t["idx5_t"], t["idx5_b"])}
</table>

{t["idx_more"]}
''')

    faq = "\n\n".join(f'<details><summary><b>{q}</b></summary>\n{a}\n</details>' for q, a in t["faq"])
    md.append(f'''<a name="faq"></a>
## {icon("q")} {t["faq_h"]}

{faq}

{pic(lang, "divider", "", 880)}

{t["footer"]}
''')
    return "\n".join(md)

for lang, out in (("en", "README.md"), ("ru", "README.ru.md")):
    path = os.path.join(BASE, out)
    open(path, "w", encoding="utf-8").write(render(lang))
    print(out, os.path.getsize(path), "bytes")
