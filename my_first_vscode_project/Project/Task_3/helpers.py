import uuid


def generate_user_data():
    """Генерирует уникальные данные пользователя для независимости тестов."""
    unique = uuid.uuid4().hex[:10]
    return {
        'email': f'user_{unique}@test.com',
        'password': f'Pass_{unique}',
        'name': f'User_{unique}',
    }


def normalize_order_number(order_number):
    """Приводит номер заказа к виду без ведущих нулей и символа #."""
    return str(int(str(order_number).replace('#', '').strip()))
