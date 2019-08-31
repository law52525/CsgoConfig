"""
    Csgo指令信息查询脚本
"""
import requests
import re
from bs4 import BeautifulSoup

while True:
    a = input("> ").strip()
    if a in ("q", "Q", "quit", "exit"):
        break
    
    r = requests.get(f"https://totalcsgo.com/commands/card/endpoint?searchTerm={a}")
    soup = BeautifulSoup(r.text, 'lxml')
    print(soup.get_text())
    print("-----Enter 'q' or 'Q' to exit.-----")