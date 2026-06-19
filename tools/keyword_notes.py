from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    """表示一个关键词笔记的数据类"""
    keyword: str
    description: str
    url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    def formatted_output(self) -> str:
        """返回格式化的笔记字符串"""
        lines = [
            f"📌 关键词：{self.keyword}",
            f"📝 描述：{self.description}",
            f"🔗 链接：{self.url or '（无）'}",
            f"🏷️ 标签：{'、'.join(self.tags) if self.tags else '（无）'}",
            f"🕒 创建时间：{self.created_at.strftime('%Y-%m-%d %H:%M')}",
        ]
        return "\n".join(lines)


def display_notes(notes: List[KeywordNote]) -> None:
    """打印所有笔记的格式化内容"""
    print("=" * 40)
    print("📚 关键词笔记列表")
    print("=" * 40)
    for i, note in enumerate(notes, 1):
        print(f"\n#{i}")
        print(note.formatted_output())
        print("-" * 30)


def find_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """根据关键词搜索笔记（不区分大小写）"""
    return [note for note in notes if keyword.lower() in note.keyword.lower()]


def find_notes_by_tag(notes: List[KeywordNote], tag: str) -> List[KeywordNote]:
    """根据标签搜索笔记"""
    return [note for note in notes if any(t.lower() == tag.lower() for t in note.tags)]


def sample_data() -> List[KeywordNote]:
    """返回一组示例笔记数据，包括指定的 URL 和关键词"""
    return [
        KeywordNote(
            keyword="雷速",
            description="雷速是一款专注于体育赛事数据与资讯的应用平台。",
            url="https://web-zhcn-leisu.com",
            tags=["体育", "数据", "资讯"],
        ),
        KeywordNote(
            keyword="Python 数据类",
            description="Python 中的 dataclass 装饰器用于简化类的定义。",
            url="https://docs.python.org/3/library/dataclasses.html",
            tags=["Python", "编程", "教程"],
        ),
        KeywordNote(
            keyword="Markdown 笔记",
            description="使用 Markdown 格式记录技术笔记，便于阅读与发布。",
            tags=["笔记", "写作", "技术"],
        ),
    ]


def main():
    notes = sample_data()
    display_notes(notes)

    print("\n🔍 搜索关键词 '雷速' 的结果：")
    found = find_notes_by_keyword(notes, "雷速")
    for note in found:
        print(note.formatted_output())

    print("\n🔍 搜索标签 'Python' 的结果：")
    tagged = find_notes_by_tag(notes, "Python")
    for note in tagged:
        print(note.formatted_output())


if __name__ == "__main__":
    main()