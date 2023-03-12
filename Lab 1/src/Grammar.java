import java.util.Random;

public class Grammar {
    Random rand = new Random();
    public String[][] rules = new String[3][4];

    Grammar(){
        setRules();
    }

    private void setRules(){
        rules[0][0] = "S";
        rules[0][1] = "aF";
        rules[0][2] = "bS";
        // 
        rules[1][0] = "F";
        rules[1][1] = "bF";
        rules[1][2] = "cD";
        rules[1][3] = "a";
        // 
        rules[2][0] = "D";
        rules[2][1] = "cS";
        rules[2][2] = "a";
    }
    
    public String generateString(){
        String newString = "S";
        for (int k = 0; k < newString.length(); k++){
            for (int i = 0; i < 3; i++){
                if (newString.charAt(k) == rules[i][0].charAt(0)){
                    int count = 0;
                    // System.out.println("start: " +newString+ " : end");
                    for (int j = 1; j < 4; j++){
                        if (rules[i][j] != null){
                            count++;
                        }
                    }
                    newString = newString.substring(0, k) + rules[i][rand.nextInt(1, count+1)];
                }
            }        
        }

        return newString;
    }
}
