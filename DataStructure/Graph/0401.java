import java.util.ArrayList;

class Solution {
    public boolean findWhetherExistsPath(int n, int[][] graph, int start, int target) {
        List<List<Integer>> adjcency = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adjcency.add(new ArrayList<>());
        }

        for (int[] node : graph) {
            int from_node = node[0];
            int to_node = node[1];
            adjcency.get(from_node).add(to_node);
        }
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(start);
        boolean[] visited = new boolean[n];
        visited[start] = true;

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (cur == target) {
                return true;
            }
            for(int neighbor : adjcency.get(cur)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.offer(neighbor);     //important:put this line inside if statement
                }
            }
        }
        return false;

    }
}