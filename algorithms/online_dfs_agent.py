from helpers import get_adjacent_states
from constants import target_state, initial_state

def online_dfs_agent():
    """
    Thuật toán DFS theo cách tiếp cận online.
    Tìm kiếm các trạng thái không hoàn chỉnh bằng cách duyệt qua các trạng thái
    dần dần khi có thêm thông tin.
    """
    def dfs(state, visited):
        # Chuyển toàn bộ trạng thái thành tuple của tuple (nếu state là list các list)
        state_tuple = tuple(tuple(substate) for substate in state)

        # Nếu trạng thái đã được duyệt qua, bỏ qua.
        if state_tuple in visited:
            return None

        # Đánh dấu trạng thái hiện tại là đã duyệt.
        visited.add(state_tuple)

        # Nếu đạt được trạng thái mục tiêu, trả về con đường
        if state == target_state:
            return [state]

        # Duyệt qua các trạng thái kề.
        for neighbor in get_adjacent_states(state):
            path = dfs(neighbor, visited)
            if path:
                return [state] + path

        return None

    # Khởi tạo tập trạng thái đã duyệt.
    visited = set()

    # Bắt đầu tìm kiếm từ trạng thái ban đầu.
    return dfs(initial_state, visited)
