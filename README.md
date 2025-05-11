# 8PuzzleSolver

## 1. Mục tiêu

Mục tiêu của bài toán là tìm ra dãy hành động (chuỗi trạng thái) để chuyển từ trạng thái ban đầu (initial state) đến trạng thái đích (goal state) trong trò chơi 8-Puzzle, sử dụng các thuật toán tìm kiếm trong trí tuệ nhân tạo. Qua đó, giúp hiểu và áp dụng các thuật toán tìm kiếm cổ điển và có heuristic, so sánh hiệu quả của các thuật toán khác nhau. Đồng thời, củng cố kiến thức về biểu diễn trạng thái, mở rộng trạng thái và hàm heuristic.

## 2. Nội dung

### 2.1. Các thuật toán Tìm kiếm không có thông tin (Uninformed Search)

#### Thành phần chính của bài toán tìm kiếm

- **Trạng thái ban đầu (Initial State):** vị trí ban đầu của các ô số trong 8-Puzzle.
- **Tập hành động (Actions):** di chuyển ô trống (lên, xuống, trái, phải).
- **Trạng thái kế tiếp (Transition Model):** trạng thái mới sau khi thực hiện một hành động.
- **Trạng thái đích (Goal State):** trạng thái mà các ô được sắp xếp đúng thứ tự.
- **Chi phí đường đi (Path Cost):** tổng số bước di chuyển từ trạng thái ban đầu đến trạng thái đích.
- **Solution:** chuỗi hành động hoặc dãy trạng thái dẫn từ trạng thái ban đầu đến đích.

| <img src="bfs.gif" width="150"/> | <img src="ids.gif" width="150"/> | <img src="ucs.gif" width="150"/> | <img src="dfs.gif" width="150"/> |
|:--------------------------------:|:--------------------------------:|:--------------------------------:|:--------------------------------:|
| **Mô phỏng BFS**                 | **Mô phỏng IDS**                 | **Mô phỏng UCS**                 | **Mô phỏng DFS**                 |
#### So sánh hiệu suất
| **Criterion**   | **Breadth-First** | **Uniform Cost** | **Depth-First** | **Depth-Bounded** | **Iterative Deepening** |
|-----------------|-------------------|------------------|------------------|---------------------|--------------------------|
| **Complete?**   | yes*              | yes              | no               | no                  | semi                     |
| **Optimal?**    | yes**             | yes              | no               | no                  | yes**                    |
| **Time**        | O(b^d)            | O(b^{⌈C*/ε⌉})     | O(b^m)           | O(b^ℓ)              | O(b^d)                   |
| **Space**       | O(b^d)            | O(b^{⌈C*/ε⌉})     | O(bm)            | O(b^ℓ)              | O(bd)                    |


### 2.2. Các thuật toán Tìm kiếm có thông tin (Informed Search)
#### Thành phần chính của bài toán tìm kiếm

- **Trạng thái ban đầu (Initial State):** vị trí ban đầu của các ô số trong 8-Puzzle.  
- **Tập hành động (Actions):** di chuyển ô trống (lên, xuống, trái, phải).  
- **Trạng thái kế tiếp (Transition Model):** trạng thái mới sau khi thực hiện một hành động.  
- **Trạng thái đích (Goal State):** trạng thái mà các ô được sắp xếp đúng thứ tự.  
- **Chi phí đường đi (Path Cost):** tổng số bước di chuyển từ trạng thái ban đầu đến trạng thái đích.  
- **Heuristic (Hàm ước lượng):** chi phí ước lượng từ trạng thái hiện tại đến đích, ví dụ: khoảng cách Manhattan.  
- **Solution:** chuỗi hành động hoặc dãy trạng thái dẫn từ trạng thái ban đầu đến đích.

| <img src="astar.gif" width="150"/> | <img src="ida.gif" width="150"/> | <img src="greedy.gif" width="150"/> |
|:----------------------------------:|:--------------------------------:|:-----------------------------------:|
| **Mô phỏng A\***                  | **Mô phỏng IDA\***              | **Mô phỏng Greedy Best-First**     |

#### So sánh các thuật toán tìm kiếm có thông tin

| **Tiêu chí**             | **Greedy Best-First Search**             | **A\***                                     | **IDA\***                                       |
|--------------------------|-------------------------------------------|----------------------------------------------|-------------------------------------------------|
| **Chiến lược**           | Chọn node có `h(n)` nhỏ nhất             | Chọn node có `f(n) = g(n) + h(n)` nhỏ nhất  | Duyệt theo DFS với ngưỡng `f_limit = g(n) + h(n)` tăng dần |
| **Cấu trúc dữ liệu**     | Priority Queue (theo `h(n)`)              | Priority Queue (theo `f(n)`)                | Stack (DFS), kết hợp lặp tăng `f_limit`         |
| **Tối ưu (Optimal)?**    |  Không                                  |  Có nếu `h(n)` admissible                 |  Có nếu `h(n)` admissible                     |
| **Hoàn tất (Complete)?** |  Không nếu không xử lý vòng lặp         |  Có nếu không có vòng vô hạn               |  Có nếu ngưỡng tăng hợp lý                    |
| **Thời gian**            | Thấp nếu heuristic tốt, nhưng dễ lạc hướng| Nhanh nếu heuristic tốt và admissible        | Có thể chậm do lặp lại nhiều                   |
| **Bộ nhớ**               | Tốn nhiều (phụ thuộc vào độ sâu và phân nhánh)| Rất tốn (O(b^d))                          | Tiết kiệm (O(d))                                |
| **Ứng dụng**             | Khi cần tốc độ, không cần kết quả tối ưu  | Khi cần giải tối ưu                         | Khi bộ nhớ hạn chế nhưng vẫn cần giải tối ưu    |


### 2.3. Các thuật toán Tìm kiếm cục bộ (Local Search)

### 2.4. Các thuật toán Tìm kiếm trong môi trường phức tạp (Complex Environments)

### 2.5. Các thuật toán Tìm kiếm CSPs - Constraint Satisfaction Problems

### 2.6. Các thuật toán Tìm kiếm Học tăng cường (Reinforcement Learning)

## 3. Kết luận
