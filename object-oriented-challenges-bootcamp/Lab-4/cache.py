class Cache:
    _MAX_CAPACITY = 0
    _MAX_CAPACITY_INITIALIZED = False

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        if not Cache._MAX_CAPACITY_INITIALIZED:
            print("Initializing MAX_CAPACITY")
            MAXC=input("Enter the maximum capacity of the cache: ")
            Cache._MAX_CAPACITY = int(MAXC)
            Cache._MAX_CAPACITY_INITIALIZED = True
        else:
            print("Returning MAX_CAPACITY")
            return Cache._MAX_CAPACITY