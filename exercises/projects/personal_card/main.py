#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 1: 个人信息卡片生成器
学习目标: 变量、字符串、f-string、print函数

项目功能:
1. 收集用户个人信息
2. 生成格式化的个人名片
3. 支持不同样式的名片
4. 保存名片到文件
"""

import datetime

def print_separator(char="=", length=40):
    """打印分隔线"""
    print(char * length)

def collect_user_info():
    """收集用户信息"""
    print_separator()
    print("🎯 欢迎使用个人名片生成器!")
    print("请输入以下信息来创建您的专属名片")
    print_separator()
    
    # 收集基本信息
    name = input("👤 请输入您的姓名: ").strip()
    age = input("🎂 请输入您的年龄: ").strip()
    job = input("💼 请输入您的职业: ").strip()
    hobbies = input("🎨 请输入您的爱好 (用逗号分隔): ").strip()
    email = input("📧 请输入您的邮箱: ").strip()
    motto = input("💭 请输入您的座右铭: ").strip()
    
    return {
        'name': name,
        'age': age,
        'job': job,
        'hobbies': hobbies,
        'email': email,
        'motto': motto
    }

def generate_card_style1(info):
    """生成经典样式名片"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    card = f"""
=======================================
           个人名片
=======================================
姓名: {info['name']}
年龄: {info['age']}岁
职业: {info['job']}
爱好: {info['hobbies']}
邮箱: {info['email']}
座右铭: {info['motto']}
=======================================
生成时间: {current_time}
=======================================
"""
    return card

def generate_card_style2(info):
    """生成现代样式名片"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    card = f"""
┌─────────────────────────────────────┐
│            🎯 个人名片              │
├─────────────────────────────────────┤
│ 👤 姓名: {info['name']:20s} │
│ 🎂 年龄: {info['age']:20s} │
│ 💼 职业: {info['job']:20s} │
│ 🎨 爱好: {info['hobbies']:20s} │
│ 📧 邮箱: {info['email']:20s} │
│ 💭 座右铭: {info['motto']:18s} │
├─────────────────────────────────────┤
│ ⏰ 生成于: {current_time:17s} │
└─────────────────────────────────────┘
"""
    return card

def generate_card_style3(info):
    """生成简约样式名片"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    card = f"""
* * * * * * * * * * * * * * * * * * * *
        {info['name']} 的个人名片
* * * * * * * * * * * * * * * * * * * *

基本信息:
  年龄: {info['age']}
  职业: {info['job']}
  邮箱: {info['email']}

兴趣爱好: {info['hobbies']}

人生格言: "{info['motto']}"

创建时间: {current_time}
* * * * * * * * * * * * * * * * * * * *
"""
    return card

def choose_card_style():
    """选择名片样式"""
    print("\n🎨 请选择名片样式:")
    print("1. 经典样式")
    print("2. 现代样式")
    print("3. 简约样式")
    
    while True:
        try:
            choice = int(input("请输入选项 (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("❌ 请输入1-3之间的数字")
        except ValueError:
            print("❌ 请输入有效的数字")

def save_card_to_file(card, filename):
    """保存名片到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(card)
        print(f"✅ 名片已保存到文件: {filename}")
        return True
    except Exception as e:
        print(f"❌ 保存文件时出错: {e}")
        return False

def main():
    """主程序"""
    print("🌟 Python 学习项目 - Day 1")
    print("个人信息卡片生成器")
    
    # 收集用户信息
    user_info = collect_user_info()
    
    # 选择样式
    style_choice = choose_card_style()
    
    # 生成名片
    if style_choice == 1:
        card = generate_card_style1(user_info)
    elif style_choice == 2:
        card = generate_card_style2(user_info)
    else:
        card = generate_card_style3(user_info)
    
    # 显示名片
    print("\n🎉 您的个人名片已生成:")
    print(card)
    
    # 询问是否保存
    save_choice = input("💾 是否保存名片到文件? (y/n): ").lower().strip()
    if save_choice in ['y', 'yes', '是']:
        filename = f"{user_info['name']}_名片_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        save_card_to_file(card, filename)
    
    print("\n🎊 感谢使用个人名片生成器!")
    print("💡 你已经完成了Python学习的第一步!")

if __name__ == "__main__":
    main()
