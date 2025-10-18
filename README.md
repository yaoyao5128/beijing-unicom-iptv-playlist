# 北京联通IPTV播放列表（每日自动更新）

## 法律声明

**使用本项目前请务必阅读[免责声明](DISCLAIMER.md)。**

## 公告

本项目将于2025年10月31日后(等作者再想起来的时候)，将 `iptv-unicast.m3u` 和 `iptv-ignored-unicast.m3u` 文件内的 `udpxy.local` 域名修改为 `iptv.local`，请您提前添加解析或修改脚本以适配更改。

## 时移

本项目已实现时移功能！时移参数参考 [APTV Playseek](https://docs.aptvapp.com/play/playseek)、[rtp2httpd Issue#25](https://github.com/stackia/rtp2httpd/issues/25)

已验证的服务端：
* [rtp2httpd](https://github.com/stackia/rtp2httpd/)(需要启用 `playseek-passthrough` [PR#23](https://github.com/stackia/rtp2httpd/issues/23))

已验证的客户端：
* [TiviMate](https://play.google.com/store/apps/details?id=ar.tvplayer.tv)，catchup格式无需修改
* [APTV](https://apps.apple.com/us/app/aptv/id1630403500)，catchup格式无需修改
* [Kodi IPTV Simple Client](https://kodi.tv/addons/omega/pvr.iptvsimple/)，catchup格式需修改为 `?playseek={utc:YmdHMS}-{utcend:YmdHMS}`
* [电视直播](https://github.com/mytv-android/mytv-android) 2.0.0.184测试版，ts2hls模式时移进度有Bug，EPG识别逻辑比较奇怪，[Issues#230](https://github.com/mytv-android/mytv-android/issues/230) 已修复对本项目EPG数据的兼容性
* [我的电视 2.2.7](https://github.com/yaoxieyoulei/mytv-android) 和 [天光云影 3.3.10](https://t.me/mytv_android_release) 不支持HTTP协议的时移，原生RTSP流待确认，其余功能完美
* [云影空蒙 3.6.5-1](https://t.me/YYKM_release/46) rtp2httpd代理的RTSP流调整时移进度有一些小Bug，ts2hls模式效果完美，本节目单项目提供的其余所有功能均完美支持

欢迎网友测试并提供反馈。

## 文件说明

* [iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u): 带有组播地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取
* [iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u): 转换为单播地址的播放列表，需要使本地网络能解析 `udpxy.local` 域名到您可访问的 `udpxy` 实例，您也可以将文件中的 `udpxy.local` 替换为您可访问的 `udpxy` 实例地址
* [iptv-unicast-timeshift-ts2hls.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast-timeshift-ts2hls.m3u.m3u): 转换为单播地址的播放列表，同上，但时移源变成了ts2hls模式
* [epg.xml](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml): 节目指南数据，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer epg.py](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/blob/main/epg.py) 抓取
* [epg.xml.gz](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml.gz): 上面那个文件的压缩版，节目单中自动调用此文件
* [playlist-raw.json](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/playlist-raw.json): 原始节目单，来自 channelAcquire 接口
* [playlist-zz.json](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/playlist-zz.json): 转换程序 `generator.py` 使用的JSON节目单
* [iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u): 无法播放频道的播放列表(组播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u): 无法播放频道的播放列表(单播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-rtsp.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp.m3u): 转换为RTSP代理地址的播放列表，需要使本地网络能解析 `iptv.local` 域名到您可访问的 `rtp2httpd` 实例，您也可以将文件中的 `iptv.local` 替换为您可访问的 `rtp2httpd` 实例地址
* [iptv-rtsp-raw.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp-raw.m3u): 带有原生RTSP地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取

## 节目单对比

|文件名称|Sniffer配置对应|地址|时移|说明|
|-----|-----|-----|-----|-----|
|[iptv-unicast-timeshift-ts2hls.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast-timeshift-ts2hls.m3u)|仅能通过 `generator.py` 生成|HTTP转组播|TS2HLS|**推荐**|
|[iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u)|playlist_save_path|HTTP转组播|HTTP转RTSP|**推荐**|
|[iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u)|playlist_mc_save_path|组播|RTSP|**推荐**，光猫路由模式可直接使用|
|[iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u)|playlist_ignored_save_path|HTTP转组播|HTTP转RTSP|已忽略的频道列表，大概没用|
|[iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u)|playlist_ignored_mc_save_path|组播|RTSP|已忽略的频道列表，大概没用|
|[iptv-rtsp.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp.m3u)|playlist_rtsp_save_path|HTTP转RTSP|HTTP转RTSP|[我的电视](https://github.com/yaoxieyoulei/mytv-android)及其分支可使用时移|
|[iptv-rtsp-raw.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp-raw.m3u)|playlist_rtsp_raw_save_path|RTSP|RTSP|光猫路由模式可直接使用，交换机组播不通时可尝试|


## 播放列表转换工具 generator.py

适用于自部署 Web 服务的情况，`generator.py` 提供三个子命令：`convert`、`serve`、`serve-fastapi`。

三个子命令均需要的信息：

* `source` 参数: 指本项目提供的 JSON 节目单文件，一般为 `playlist-zz.json`，支持指定多个文件，会按照字典键合并live和timeshift中的数据，您可参照该格式附加其余地域或添加其它源
* `--key-live` 参数: 指定直播源的键名 (JSON 节目单文件中每个频道中 live 下的键名)，本项目提供了 `bjunicom-multicast` 和 `bjunicom-rtsp`
* `--key-timeshift` 参数: 指定时移源的键名 (JSON 节目单文件中每个频道中 timeshift 下的键名)，本项目提供了 `bjunicom-rtsp`
* HTTP `live` 参数: 同 `--key-live`，指定多个时请使用英文逗号隔开。
* HTTP `timeshift` 参数: 同 `--key-timeshift`，指定多个时请使用英文逗号隔开。

键名说明：当源的类型为 `rtp` 和 `rtsp` 时，可在原始键名后添加 `-httpproxy` 将播放地址转换为代理格式，当源的类型为 `rtsp` 时，可在原始键名后添加 `-ts2hls` 将播放地址转换为ts2hls格式。

所以本项目提供的数据中可用的 Key 值如下：

| Key                            | 直播/时移 | 解释                                                     |
|--------------------------------|-----------|----------------------------------------------------------|
| `bjunicom-multicast`           | 仅直播    | 组播直播源                                               |
| `bjunicom-multicast-httpproxy` | 仅直播    | 由 udpxy 或 rtp2httpd 代理的组播直播源                   |
| `bjunicom-rtsp`                | 直播+时移 | RTSP 直播源，**不推荐用于直播**                          |
| `bjunicom-rtsp-httpproxy`      | 直播+时移 | 由 rtp2httpd 代理的 RTSP 直播源，**不推荐用于直播**      |
| `bjunicom-rtsp-ts2hls`         | 直播+时移 | 由 RTSP 地址转换成的 TS2HLS 地址，**非常不推荐用于直播** |

命令帮助信息：

```shell
$ python3 generator.py --help
usage: generator.py [-h] {serve,serve-fastapi,convert} ...

Generate M3U playlist from ZZ JSON playlist(s).

positional arguments:
  {serve,serve-fastapi,convert}
    serve               Use flask to serve playlist.
    serve-fastapi       Use FastAPI to serve playlist.
    convert             Convert playlist format.

options:
  -h, --help            show this help message and exit
```

示例见下文。

### convert 子命令 - 转换播放列表

用于将 JSON 格式的播放列表转换为 M3U 格式。

基本用法：

```bash
$ python generator.py convert playlist-zz.json --output iptv.m3u
```

完整示例（假设您的服务器 IP 地址为 10.1.1.1，并且在该服务器上安装了 udpxy 和 Nginx）：

```bash
$ python generator.py convert playlist-zz.json \
  --key-live bjunicom-multicast-httpproxy bjunicom-rtsp-ts2hls \
  --key-timeshift bjunicom-rtsp-ts2hls bjunicom-rtsp \
  --rtp-proxy-url http://10.1.1.1:8081/rtp/ \
  --rtsp-proxy-url http://10.1.1.1:8081/rtsp/ \
  --epg-url http://10.1.1.1:8081/epg.xml.gz \
  --logo-url http://10.1.1.1:8081/img/ \
  --output iptv.m3u
```

常用参数：
* `--key-live`: 指定直播源（默认：`bjunicom-multicast`）
* `--key-timeshift`: 指定时移源（默认：`bjunicom-rtsp`）
* `--rtp-proxy-url`: RTP 代理地址（默认：`http://iptv.local:8080/rtp/`）
* `--rtsp-proxy-url`: RTSP 代理地址（默认：`http://iptv.local:8080/rtsp/`）
* `--multi-source`: 启用多源模式
* `--tag-include`: 仅包含特定标签的频道（默认：无）
* `--tag-exclude`: 排除特定标签的频道（默认：`ignore`）
* `--catchup-param`: 时移参数格式（默认：`playseek=${(b)yyyyMMddHHmmss}-${(e)yyyyMMddHHmmss}`，可设为 `kodi` 以兼容 Kodi）

子命令帮助信息：

```shell
$ python3 generator.py convert --help
usage: generator.py convert [-h] [--key-live KEY_LIVE [KEY_LIVE ...]] [--key-timeshift KEY_TIMESHIFT [KEY_TIMESHIFT ...]] [--rtp-proxy-url RTP_PROXY_URL] [--rtsp-proxy-url RTSP_PROXY_URL] [--multi-source] [--tag-include TAG_INCLUDE [TAG_INCLUDE ...]]
                            [--tag-exclude TAG_EXCLUDE [TAG_EXCLUDE ...]] [--keep-channel-acquire-name] [--epg-url EPG_URL] [--logo-url LOGO_URL] [--catchup-param CATCHUP_PARAM] [--output OUTPUT]
                            source [source ...]

positional arguments:
  source                Path(s) to ZZ JSON playlist file(s).

options:
  -h, --help            show this help message and exit
  --key-live KEY_LIVE [KEY_LIVE ...]
                        Keys for live sources to include.
  --key-timeshift KEY_TIMESHIFT [KEY_TIMESHIFT ...]
                        Keys for timeshift sources to include.
  --rtp-proxy-url RTP_PROXY_URL
                        RTP proxy URL.
  --rtsp-proxy-url RTSP_PROXY_URL
                        RTSP proxy URL.
  --multi-source        Enable multi source mode.
  --tag-include TAG_INCLUDE [TAG_INCLUDE ...]
                        Only include channels with these tags.
  --tag-exclude TAG_EXCLUDE [TAG_EXCLUDE ...]
                        Exclude channels with these tags.
  --keep-channel-acquire-name
                        Use channel name from channelAcquire API
  --epg-url EPG_URL     EPG URL.
  --logo-url LOGO_URL   Logo URL.
  --catchup-param CATCHUP_PARAM
                        Catchup parameter.
  --output OUTPUT       Output M3U playlist file path.
```

### serve 子命令 - Flask Web 服务

通过 Flask 提供动态 M3U 播放列表服务，支持通过 URL 参数自定义配置，可结合 `generator.html` 使用。

基本用法：
```bash
$ python generator.py serve playlist-zz.json --listen 127.0.0.1 --port 5000 --base-url "http://10.1.1.1:8081"
```

启动参数：
* `--listen`: 监听地址
* `--port`: 监听端口
* `--base-url`: EPG和Logo的基础URL，默认使用GitHub

接口地址：`http://服务器IP:5000/playlist.m3u`，可通过仓库中提供的 `generator.html` 调用

支持的 URL 参数：
* `live`: 直播源键，多个用逗号分隔
* `timeshift`: 时移源键，多个用逗号分隔
* `host`: 代理服务器地址（与 `scheme`、`port`、`rtp`、`rtsp` 配合使用）
* `scheme`: 协议（http/https，默认 http）
* `port`: 端口号
* `rtp`: RTP 路径（默认 `rtp`）
* `rtsp`: RTSP 路径（默认 `rtsp`）
* `multisource`: 启用多源（`1`/`true`）
* `include`: 包含标签，多个用逗号分隔
* `exclude`: 排除标签，多个用逗号分隔
* `epg`: EPG 地址（支持相对路径、完整 URL 或 `0` 禁用）
* `logo`: 台标地址（支持相对路径、完整 URL 或 `0` 禁用）
* `catchup`: 时移参数格式
* `txt`: 设为 `1` 时返回纯文本格式

示例：`http://10.1.1.1:5000/playlist.m3u?host=10.1.1.1&port=8081&live=bjunicom-multicast-httpproxy`

子命令帮助信息：

```shell
$ python3 generator.py serve --help
usage: generator.py serve [-h] [--listen LISTEN] [--port PORT] [--base-url BASE_URL] source [source ...]

positional arguments:
  source               Path(s) to ZZ JSON playlist file(s).

options:
  -h, --help           show this help message and exit
  --listen LISTEN      IP address to listen on.
  --port PORT          Port to serve on.
  --base-url BASE_URL  Base URL for EPG and logo if relative paths are used.
```

### serve-fastapi 子命令 - FastAPI Web 服务

与 `serve` 功能相同，但使用 FastAPI 框架。

基本用法：
```bash
$ python generator.py serve-fastapi playlist-zz.json --listen 127.0.0.1 --port 5000 --base-url "http://10.1.1.1:8081"
```

需要安装依赖：`pip install fastapi uvicorn`

子命令帮助信息：

```shell
$ python3 generator.py serve-fastapi --help
usage: generator.py serve-fastapi [-h] [--listen LISTEN] [--port PORT] [--base-url BASE_URL] source [source ...]

positional arguments:
  source               Path(s) to ZZ JSON playlist file(s).

options:
  -h, --help           show this help message and exit
  --listen LISTEN      IP address to listen on.
  --port PORT          Port to serve on.
  --base-url BASE_URL  Base URL for EPG and logo if relative paths are used.
```

### Nginx 配置示例

```
server {
    listen 8081;
    #server_name 10.1.1.1;
    # root 指定为本项目根目录
    root /var/www/iptv;

    # 指向 udpxy
    location /rtp {
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:8080;
    }
    
    # 如果您使用了 rtp2httpd 或其他能代理 rtsp 协议的软件
    location /rtsp {
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:8080;
    }

    # 如果您运行了 generator.py serve 提供的实例
    location = /playlist.m3u {
        proxy_pass http://127.0.0.1:5000/playlist.m3u;
    }
}
```

配置仅供参考，请按实际情况修改，并且将更新仓库和转换的命令放在 crontab 中定时执行。

## 播放列表转换工具 convert.py

**⚠️ 注意：此方法已弃用，未来可能删除，请使用 `generator.py convert` 代替。**

适用于自部署 Web 服务的情况，以下示例假设您的服务器 IP 地址为 10.1.1.1，并且在该服务器上安装了 udpxy 和 Nginx

转换: `./convert.py --rtp-url http://10.1.1.1:8081/rtp/ --epg-url http://10.1.1.1:8081/epg.xml.gz --logo-url http://10.1.1.1:8081/img/ --output iptv.m3u`

## 致谢

本项目台标资源来源于互联网，部分台标资源来源于 [老张的EPG](http://epg.51zmt.top:8000/) 、 [wanglindl/TVlogo](https://github.com/wanglindl/TVlogo) 、 [EPG-电子节目单](https://epg.112114.xyz/) 项目，在此向项目维护者表示感谢。
