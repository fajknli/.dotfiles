#!/usr/bin/env python3

# Author:       fajknli
# Emial         fajknli@gmail.com
# Created Time: 2025-08-14 00:46
# Filename:     gmn4.py


import requests
from urllib.parse import unquote
import time
import random

class NetEaseMusic:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://music.163.com/'
        }
        # 替换为你手动获取的Cookie
        self.cookies = {
            'MUSIC_U': '0016EC35B9C9C9F0BA60E58B9185A54DFFC4BEC37FFE609AB09106F17A6404BAA3B18A96BF724403709E22B5AE8F9F3FFCC7AE5381729082781AF53D7B806E49571CC57AAD067173F07CF611A994A5463703569B1F9273DC67C9B1F61865A6EA6B2E3CE4BFD97F74D9410B9823AB4FFE91883D31859F65CA24469D497BBC324297AF0EF764E17B9F9DC4F0677BB4AC20321F02D6E85D8B031029B44AB07D58F90EB10142289402FD6142A47EFE94C3737002F2E21A61DC7B5E528E3D59999F1884ADA390D7B85ECE8EB1D57383F3B46A0D4B4D4609ADB6A45D17566DC4AF5B9B3BAB50769B3DED02E6728C904E5F7BA8E3252773EFBCF9524050CAB128B24893242E8CF1883E2402E9773376D7C18EDE3E2B1E389FEEB7EEEF045949AA2E56F630E59822780C9FA1CFFA471CF7C5588935BD1D88A1C7F66F85D406FA48D6DC0CD2BF86FC499D7425EBC386FF734D4334BD45CD4C43871958A443B45DEE3F039DE65A948974286975E39743CFC9E9828A1B5CD0C3D239BE4FEB2583D340365F0EC1',
            '__csrf': '8066a9e6745a88a548c6a90045e76e1b',
            'NMTID': '00O9aWfTQmnLwhdU0LQliDCniWxXlQAAAGYo2PL-Q'
        }

    def get_full_playlist(self, playlist_id):
        """获取完整歌单"""
        url = 'https://music.163.com/api/v6/playlist/detail'
        params = {
            'id': playlist_id,
            'n': 10000,
            's': 8
        }

        try:
            response = self.session.get(
                url,
                headers=self.headers,
                params=params,
                cookies=self.cookies,
                timeout=10
            )
            data = response.json()

            if data['code'] != 200:
                print(f"获取失败: {data.get('message')}")
                return None

            return data['playlist']['tracks']
        except Exception as e:
            print(f"请求失败: {str(e)}")
            return None

    def get_song_url(self, song_id):
        """获取歌曲播放链接"""
        url = f'https://music.163.com/song/media/outer/url?id={song_id}.mp3'
        try:
            response = self.session.get(
                url,
                headers=self.headers,
                cookies=self.cookies,
                allow_redirects=False,
                timeout=10
            )
            if response.status_code in (301, 302):
                return unquote(response.headers['Location'])
            return url
        except Exception as e:
            print(f"获取链接失败: {str(e)}")
            return None

def main():
    netease = NetEaseMusic()

    playlist_id = input("请输入歌单ID: ")
    print("\n正在获取歌单信息...")

    songs = netease.get_full_playlist(playlist_id)
    if not songs:
        print("获取歌单失败")
        return

    # 显示基本信息
    info_url = f'https://music.163.com/api/v3/playlist/detail?id={playlist_id}'
    info = netease.session.get(info_url).json()['playlist']

    print(f"\n歌单名称: {info['name']}")
    print(f"创建者: {info['creator']['nickname']}")
    print(f"歌曲数量: {info['trackCount']}")
    print(f"播放次数: {info['playCount']}")
    print(f"收藏数: {info['subscribedCount']}")
    print("\n前20首歌曲:")

    for idx, song in enumerate(songs[:20], 1):
        artists = ", ".join([ar['name'] for ar in song['ar']])
        print(f"{idx}. {song['name']} - {artists}")

    # 保存全部歌曲
    save = input("\n是否保存全部歌曲链接? (y/n): ").lower()
    if save != 'y':
        return

    filename = f"{info['name']}_歌曲列表.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for idx, song in enumerate(songs, 1):
            url = netease.get_song_url(song['id'])
            artists = ", ".join([ar['name'] for ar in song['ar']])
            f.write(f"{idx}. {song['name']} - {artists}\n")
            if url:
                f.write(f"播放链接: {url}\n")
            f.write("\n")
            print(f"已处理: {idx}/{len(songs)} {song['name']}")
            time.sleep(random.uniform(0.5, 1.5))

    print(f"\n所有{len(songs)}首歌曲已保存到 {filename}")

if __name__ == "__main__":
    main()
