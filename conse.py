def perform_operation():
    try:
        # Perform some operations
        status = True  # Operation succeeded
    except Exception as e:
        status = False  # Operation failed
    return status

# Calling the function
operation_status = perform_operation()
print("Operation status:", operation_status)
