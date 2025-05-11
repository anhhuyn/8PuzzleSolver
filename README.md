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
#### Đặc điểm của tìm kiếm cục bộ

- Không lưu trữ toàn bộ đường đi từ trạng thái ban đầu đến trạng thái đích.
- Chỉ quan tâm đến trạng thái hiện tại và các trạng thái lân cận.
- Hiệu quả với không gian trạng thái lớn hoặc vô hạn.
- Không đảm bảo tìm được lời giải tối ưu.

| <img src="simple_hill_climbing.gif" width="150"/> | <img src="steepest_ascent_hill_climbing.gif" width="150"/> | <img src="stochastic_hill_climbing.gif" width="150"/> | <img src="simulated_annealing.gif" width="150"/> | <img src="beam_search.gif" width="150"/> | <img src="genetic_algorithm.gif" width="150"/> |
|:--------------------------------------:|:-------------------------------------:|:---------------------------------------:|:-------------------------------------:|:------------------------------:|:------------------------------------:|
| **Simple Hill Climbing**              | **Steepest Ascent Hill Climbing**    | **Stochastic Hill Climbing**           | **Simulated Annealing (SA)**         | **Beam Search (k=5)**         | **Genetic Algorithm (GA)**           |

#### So sánh hiệu suất

| **Thuật toán**              | **Nguyên lý hoạt động**                                                                 | **Ưu điểm**                                           | **Nhược điểm**                                                 |
|----------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------|----------------------------------------------------------------|
| **Simple Hill Climbing**   | Di chuyển đến trạng thái lân cận tốt hơn hiện tại.                                      | Đơn giản, dễ cài đặt                                 | Dễ bị kẹt ở đỉnh cục bộ hoặc cao nguyên                        |
| **Steepest Ascent HC**     | Xét tất cả các lân cận, chọn trạng thái tốt nhất.                                       | Tăng khả năng tìm được trạng thái tốt hơn            | Tốn thời gian kiểm tra, vẫn có thể kẹt                         |
| **Stochastic HC**          | Chọn ngẫu nhiên một trạng thái tốt hơn trong số các lân cận.                            | Giảm xác suất bị kẹt ở cao nguyên                    | Kết quả không ổn định, phụ thuộc ngẫu nhiên                    |
| **Simulated Annealing**    | Đôi khi chấp nhận trạng thái kém hơn để thoát khỏi đỉnh cục bộ, xác suất giảm theo thời gian. | Có thể vượt qua đỉnh cục bộ                          | Cần điều chỉnh tham số (nhiệt độ), có thể chậm                 |
| **Beam Search (k=5)**      | Duy trì k trạng thái tốt nhất ở mỗi bước.                                               | Cân bằng hiệu quả và chất lượng lời giải            | Có thể bỏ lỡ lời giải tốt nếu không nằm trong beam             |
| **Genetic Algorithm (GA)** | Mô phỏng tiến hóa sinh học: chọn lọc, lai ghép, đột biến để tạo thế hệ mới.             | Khả năng khám phá không gian rộng, lời giải đa dạng | Phức tạp, cần tinh chỉnh tham số                              |

### 2.4. Các thuật toán Tìm kiếm trong môi trường phức tạp (Complex Environments)

### 2.5. Các thuật toán Tìm kiếm CSPs - Constraint Satisfaction Problems

### 2.6. Các thuật toán Tìm kiếm Học tăng cường (Reinforcement Learning)

## 3. Kết luận
