"""
公共工具函数库
包含各个项目中可能用到的通用函数
"""

import os
import datetime
import json


def print_separator(char="=", length=50):
    """打印分隔线"""
    print(char * length)


def print_title(title, char="="):
    """打印标题"""
    print_separator(char)
    print(f" {title} ".center(50, char))
    print_separator(char)


def get_user_input(prompt, input_type=str, validator=None):
    """
    获取用户输入并进行类型转换和验证
    
    Args:
        prompt: 提示信息
        input_type: 输入类型 (str, int, float)
        validator: 验证函数
    
    Returns:
        转换后的用户输入
    """
    while True:
        try:
            user_input = input(prompt)
            converted_input = input_type(user_input)
            
            if validator and not validator(converted_input):
                print("输入不符合要求，请重新输入。")
                continue
                
            return converted_input
        except ValueError:
            print(f"请输入有效的{input_type.__name__}类型数据。")


def save_to_file(data, filename, mode='w'):
    """保存数据到文件"""
    try:
        with open(filename, mode, encoding='utf-8') as f:
            if isinstance(data, (dict, list)):
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                f.write(str(data))
        print(f"数据已保存到 {filename}")
        return True
    except Exception as e:
        print(f"保存文件时出错: {e}")
        return False


def load_from_file(filename):
    """从文件加载数据"""
    try:
        if not os.path.exists(filename):
            return None
            
        with open(filename, 'r', encoding='utf-8') as f:
            # 尝试作为JSON加载
            try:
                f.seek(0)
                return json.load(f)
            except json.JSONDecodeError:
                # 如果不是JSON，作为文本加载
                f.seek(0)
                return f.read()
    except Exception as e:
        print(f"加载文件时出错: {e}")
        return None


def get_current_time(format_str="%Y-%m-%d %H:%M:%S"):
    """获取当前时间字符串"""
    return datetime.datetime.now().strftime(format_str)


def create_menu(options, title="请选择"):
    """
    创建菜单并获取用户选择
    
    Args:
        options: 选项列表
        title: 菜单标题
    
    Returns:
        用户选择的选项索引
    """
    print_title(title)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("0. 退出")
    
    while True:
        try:
            choice = int(input("\n请输入选项号码: "))
            if 0 <= choice <= len(options):
                return choice
            else:
                print("无效选项，请重新输入。")
        except ValueError:
            print("请输入数字。")


def format_currency(amount):
    """格式化货币显示"""
    return f"¥{amount:,.2f}"


def calculate_percentage(part, total):
    """计算百分比"""
    if total == 0:
        return 0
    return (part / total) * 100


def validate_email(email):
    """简单的邮箱验证"""
    return "@" in email and "." in email.split("@")[-1]


def validate_phone(phone):
    """简单的手机号验证"""
    return len(phone) == 11 and phone.isdigit()


# 装饰器函数
def timer(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper


def retry(max_attempts=3):
    """重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"第{attempt + 1}次尝试失败: {e}")
            return None
        return wrapper
    return decorator


if __name__ == "__main__":
    # 测试函数
    print_title("公共工具函数测试")
    print(f"当前时间: {get_current_time()}")
    print(f"格式化货币: {format_currency(1234.56)}")
    print(f"百分比计算: {calculate_percentage(25, 100):.1f}%")
    print(f"邮箱验证: {validate_email('test@example.com')}")
    print(f"手机号验证: {validate_phone('13800138000')}")
