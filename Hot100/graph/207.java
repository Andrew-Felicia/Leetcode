class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> gragh = new HashMap<>();
        int[] in_degree = new int[numCourses];
        for(int[] pair : prerequisites) {
            int course = pair[0];
            int prereq = pair[1];
            gragh.computeIfAbsent(prereq, k -> new ArrayList<>()).add(course);
            in_degree[course] ++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++) {
            if(in_degree[i] == 0) {
                queue.offer(i);
            }
        }

        int visited_courses = 0;
        while(!queue.isEmpty()) {
            int current_course = queue.poll();
            visited_courses += 1;
            List<Integer> neighbor = gragh.getOrDefault(current_course, new ArrayList<>());

            for(int next : neighbor) {
                in_degree[next] -= 1;
                if(in_degree[next] == 0) {
                    queue.offer(next);
                }
            }
        }

        return visited_courses == numCourses;
    }
}