import re

import requests

proxies = {
    "http": "http://192.168.31.2:7899",
    "https":  "http://192.168.31.2:7899",
}
def analyse_bilibili_url(url):
    cookies = {
        "buvid3": "9110FF74-D828-C939-C0B1-9BCA1BA2100211467infoc",
        "b_nut": "1675145311",
        "i-wanna-go-back": "-1",
        "_uuid": "DE410C1E9-F5E6-D298-4D96-A1A10643226FF12760infoc",
        "buvid4": "2300305A-D0DF-3E76-3B60-635DD47CEC6C17499-023013114-o4YItRKtRPydLGcqbR5tIw%3D%3D",
        "buvid_fp_plain": "undefined",
        "DedeUserID": "1960252",
        "DedeUserID__ckMd5": "cab101b59c8e7942",
        "CURRENT_BLACKGAP": "0",
        "rpdid": "|(Jlkl~~l~k|0J'uY~luRlRu~",
        "CURRENT_FNVAL": "4048",
        "b_ut": "5",
        "theme_style": "light",
        "nostalgia_conf": "-1",
        "LIVE_BUVID": "AUTO3716760987006347",
        "header_theme_version": "CLOSE",
        "home_feed_column": "5",
        "theme_style": "light",
        "CURRENT_PID": "eef85f40-cec4-11ed-8e2a-13ed54fabef6",
        "PVID": "1",
        "share_source_origin": "QQ",
        "FEED_LIVE_VERSION": "V8",
        "SESSDATA": "cba7b2a2%2C1696931488%2C6c414%2A42",
        "bili_jct": "70d4a330bdda0d12692b819df26a04c8",
        "b_lsid": "3466C2B10_1877A738BF1",
        "innersign": "1",
        "sid": "8kozby3o",
        "fingerprint": "7e14bf5eefd6b94ba0ac9eaf2acaafce",
        "bsource": "search_google",
        "buvid_fp": "7e14bf5eefd6b94ba0ac9eaf2acaafce",
        "bp_video_offset_1960252": "784041882072121300",
    }

    headers = {
        "authority": "www.bilibili.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        # 'cookie': "buvid3=9110FF74-D828-C939-C0B1-9BCA1BA2100211467infoc; b_nut=1675145311; i-wanna-go-back=-1; _uuid=DE410C1E9-F5E6-D298-4D96-A1A10643226FF12760infoc; buvid4=2300305A-D0DF-3E76-3B60-635DD47CEC6C17499-023013114-o4YItRKtRPydLGcqbR5tIw%3D%3D; buvid_fp_plain=undefined; DedeUserID=1960252; DedeUserID__ckMd5=cab101b59c8e7942; CURRENT_BLACKGAP=0; rpdid=|(Jlkl~~l~k|0J'uY~luRlRu~; CURRENT_FNVAL=4048; b_ut=5; theme_style=light; nostalgia_conf=-1; LIVE_BUVID=AUTO3716760987006347; header_theme_version=CLOSE; home_feed_column=5; theme_style=light; CURRENT_PID=eef85f40-cec4-11ed-8e2a-13ed54fabef6; PVID=1; share_source_origin=QQ; FEED_LIVE_VERSION=V8; SESSDATA=cba7b2a2%2C1696931488%2C6c414%2A42; bili_jct=70d4a330bdda0d12692b819df26a04c8; b_lsid=3466C2B10_1877A738BF1; innersign=1; sid=8kozby3o; fingerprint=7e14bf5eefd6b94ba0ac9eaf2acaafce; bsource=search_google; buvid_fp=7e14bf5eefd6b94ba0ac9eaf2acaafce; bp_video_offset_1960252=784041882072121300",
        "pragma": "no-cache",
        "referer": "https://www.bilibili.com/",
        "sec-ch-ua": '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34",
    }

    params = {
        # 'spm_id_from': '333.1007.tianma.3-3-9.click',
        # 'vd_source': '68eb919d832e2b2d4630c7f866e5f3bb',
    }
    print("获取字幕url中")
    response = requests.get(
        url,
        params=params,
        cookies=cookies,
        headers=headers,
    )
    subtitle_url = re.findall(r'"subtitle_url":"([^"]*)', response.text)
    if not subtitle_url:
        raise Exception("该视频没有自动字幕")
    print("获取字幕url完毕")
    subtitle = requests.get(subtitle_url[0].replace("\\u002F", "/")).json()
    print("获取字幕内容完毕")
    subtitle_content = [i["content"] for i in subtitle["body"]]
    OPENAI_API_KEY = "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"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + OPENAI_API_KEY,
    }

    json_data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": "Please help me analyze the abstract of the following subtitle content, and translate it into Chinese:\n"
                + "\n".join(subtitle_content),
            },
        ],
    }
    print("开始发给OpenAI")
    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=json_data, proxies=proxies,
    )
    if (
        response.status_code == 400
        and response.json()["error"]["code"] == "context_length_exceeded"
    ):
        raise Exception("字幕内容过长，暂时无法分析\n" + response.json()["error"]["message"])
    return response.json()["choices"]


if __name__ == "__main__":
    # url = "https://www.bilibili.com/video/BV1zX4y167MQ/"
    url = "https://www.bilibili.com/video/BV1EM4y1U7Te/?spm_id_from=333.1007.tianma.8-4-30.click&vd_source=68eb919d832e2b2d4630c7f866e5f3bb"
    print(analyse_bilibili_url(url))
