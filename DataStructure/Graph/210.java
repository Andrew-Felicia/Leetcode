import java.util.List;
import java.util.ArrayList;
import java.util.Queue;
import java.util.ArrayDeque;


class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> gragh = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            gragh.add(new ArrayList<>());
        }

        int[] indegree = new int[numCourses];
        Arrays.fill(indegree, 0);
        for (int[] pair : prerequisites) {
            int course = pair[0];
            int pre = pair[1];
            gragh.get(pre).add(course);
            indegree[course] += 1;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        int[] result = new int[numCourses];
        int index = 0;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        while (!queue.isEmpty()) {
            int cur = queue.poll();
            result[index++] = cur;

            for (int nextCourse : gragh.get(cur)) {
                indegree[nextCourse] -= 1;
                if (indegree[nextCourse] == 0) {
                    queue.offer(nextCourse);
                }
            }
        }

        return index == numCourses ? result : new int[0];
    }
}