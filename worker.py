from workers import WorkerEntrypoint, Response
from urllib.parse import urlparse, parse_qsl
import traceback
import os
import sys
from generator import generate_m3u_from_http_get_params

class Default(WorkerEntrypoint):
    async def fetch(self, request, env):
        url = urlparse(request.url)
        try:
            if url.path == "/playlist.m3u":
                args = dict(parse_qsl(url.query))
                txt = generate_m3u_from_http_get_params(
                    json_path_list=["/session/metadata/playlist-zz.json"],
                    args=args
                )
                return Response(txt, headers={
                    "Content-Type": "text/plain; charset=utf-8" if args.get("txt", "0") == "1" else "application/x-mpegURL; charset=utf-8"
                })
        except Exception as e:
            error_message = traceback.format_exc()
            return Response(error_message, status=500, headers={
                "Content-Type": "text/plain"
            })
        return await self.env.ASSETS.fetch(request)