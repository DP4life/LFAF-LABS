public class Main {
	public static void main(String[] args) {
		Grammar grammar = new Grammar();
		DFA dfa = new DFA();
		// grammar.printRules();
		String[] sarray = new String[5];

		for (int i = 0; i < 5; i++) {
			String newString = grammar.generateString();

			// Check if the new string is already in the array
			while (isStringInArray(newString, sarray)) {
				newString = grammar.generateString(); // Generate a new string
			}

			// Add the new string to the array
			sarray[i] = newString;
			System.out.println(sarray[i] + " - " + dfa.accepts(sarray[i]));
		}

	}

	public static boolean isStringInArray(String str, String[] arr) {
		for (String s : arr) {
			if (str.equals(s)) {
				return true;
			}
		}
		return false;
	}

}
