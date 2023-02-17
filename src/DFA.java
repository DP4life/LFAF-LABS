public class DFA {
    public boolean accepts(String s) {
        int current_state = 0;
        int[][] delta = {
            {1, 0, -1}, 
            {3, 1, 2}, 
            {3, -1, 0},
            {-1, -1, -1},  //accepting state
            {-1, -1, -1} //error state
        };
        int accepting_state = 3;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int input;
            if (c == 'a') {
                input = 0;
            } else if (c == 'b') {
                input = 1;
            } else if (c == 'c') {
                input = 2;
            } else {
                // Input symbol not in the alphabet
                return false;
            }
            int next_state = delta[current_state][input];
            if (next_state == -1) {
                // Entered error state
                return false;
            }
            current_state = next_state;
        }

        return current_state == accepting_state;
    }
}
