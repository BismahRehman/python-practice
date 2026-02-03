class AppError(Exception):
    """Base class for all custom errors"""
    pass


class ValidationError(AppError):
    pass


class UserNotFoundError(AppError):
    pass
def get_user(user_id):
    if user_id <= 0:
        raise ValidationError("User ID must be positive")

    user = None  # imagine DB lookup
    if user is None:
        raise UserNotFoundError(f"User {user_id} not found")

    return user
try:
    user = get_user(5)
except UserNotFoundError as e:
    print(f"Not found: {e}")
except ValidationError as e:
    print(f"Invalid input: {e}")
except AppError as e:
    print(f"App error: {e}")
except Exception as e:
    print("Unexpected error:", e)

def main():
    user = get_user(-1)
    print(user)

if __name__ == "__main__":
    try:
        main()
    except AppError as e:
        print(f"Error: {e}")
    except Exception:
        print("Something went very wrong")

