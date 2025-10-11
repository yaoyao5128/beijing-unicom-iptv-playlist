# 北京联通IPTV播放列表（每日自动更新）

## 法律声明

**使用本项目前请务必阅读[免责声明](DISCLAIMER.md)。**

## 公告

本项目将于2025年10月31日后(等作者再想起来的时候)，将 `iptv-unicast.m3u` 和 `iptv-ignored-unicast.m3u` 文件内的 `udpxy.local` 域名修改为 `iptv.local`，请您提前添加解析或修改脚本以适配更改。

## 时移

本项目已实现时移功能！

已验证的服务端：
* [rtp2httpd](https://github.com/stackia/rtp2httpd/)(需要启用 `playseek-passthrough` [PR#25](https://github.com/stackia/rtp2httpd/issues/25))

已验证的客户端：
* [Kodi IPTV Simple Client](https://kodi.tv/addons/omega/pvr.iptvsimple/)，catchup格式需修改为 `?playseek={utc:YmdHMS}-{utcend:YmdHMS}`
* [TiviMate](https://play.google.com/store/apps/details?id=ar.tvplayer.tv)，catchup格式配置文件默认即可，参考 [APTV Playseek](https://docs.aptvapp.com/play/playseek)
* [我的电视](https://github.com/yaoxieyoulei/mytv-android) 、[电视直播](https://github.com/mytv-android/mytv-android) 和 天光云影 仅支持rtp2httpd代理的RTSP流且无法调整回放进度，似乎未识别m3u catchup参数，原生RTSP流待确认。

欢迎网友测试并提供反馈。

## 文件说明

* [iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u): 带有组播地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取
* [iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u): 转换为单播地址的播放列表，需要使本地网络能解析 `udpxy.local` 域名到您可访问的 `udpxy` 实例，您也可以将文件中的 `udpxy.local` 替换为您可访问的 `udpxy` 实例地址
* [epg.xml](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml): 节目指南数据，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer epg.py](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/blob/main/epg.py) 抓取
* [epg.xml.gz](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml.gz): 上面那个文件的压缩版，节目单中自动调用此文件
* [rawplaylist.json](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/rawplaylist.json): 原始节目单
* [iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u): 无法播放频道的播放列表(组播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u): 无法播放频道的播放列表(单播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-rtsp.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp.m3u): 转换为RTSP代理地址的播放列表，需要使本地网络能解析 `iptv.local` 域名到您可访问的 `rtp2httpd` 实例，您也可以将文件中的 `iptv.local` 替换为您可访问的 `rtp2httpd` 实例地址
* [iptv-rtsp-raw.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp-raw.m3u): 带有原生RTSP地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取

## 节目单对比

|文件名称|Sniffer配置对应|地址|时移|说明|
|-----|-----|-----|-----|-----|
|[iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u)|playlist_save_path|HTTP转组播|HTTP转RTSP|**推荐**|
|[iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u)|playlist_mc_save_path|组播|RTSP|**推荐**，光猫路由模式可直接使用|
|[iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u)|playlist_ignored_save_path|HTTP转组播|HTTP转RTSP|已忽略的频道列表，大概没用|
|[iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u)|playlist_ignored_mc_save_path|组播|RTSP|已忽略的频道列表，大概没用|
|[iptv-rtsp.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp.m3u)|playlist_rtsp_save_path|HTTP转RTSP|HTTP转RTSP|[我的电视](https://github.com/yaoxieyoulei/mytv-android)及其分支可使用时移|
|[iptv-rtsp-raw.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-rtsp-raw.m3u)|playlist_rtsp_raw_save_path|RTSP|RTSP|光猫路由模式可直接使用，交换机组播不通时可尝试|


## 播放列表转换工具 convert.py

适用于自部署 Web 服务的情况，以下示例假设您的服务器 IP 地址为 10.1.1.1，并且在该服务器上安装了 udpxy 和 Nginx

转换: `./convert.py --rtp-url http://10.1.1.1:8081/rtp/ --epg-url http://10.1.1.1:8081/epg.xml.gz --logo-url http://10.1.1.1:8081/img/ --output iptv.m3u`

然后将整个目录使用 Nginx 等工具承载即可，以下是一个示例的 Nginx 虚拟主机配置文件

```
server {
    listen 8081;
    #server_name 10.1.1.1;
    root /var/www/iptv;

    location /rtp {
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:8080;
    }
}
```

配置仅供参考，请按实际情况修改，并且将更新仓库和转换的命令放在crontab中定时执行。

## 致谢

本项目台标资源来源于互联网，部分台标资源来源于 [老张的EPG](http://epg.51zmt.top:8000/) 和 [wanglindl/TVlogo](https://github.com/wanglindl/TVlogo) 项目，在此向项目维护者表示感谢。
