public String replaceWords(List<String> dictionary, String sentence) {
        String[] words = sentence.split("");

        //load dic into hashmap
        Map<String,String> dict = new HashMap<String,String>();
        for(int x =0; x < dictionary.size(); x++){
            dict.put(dictionary.get(x),dictionary.get(x));
        }

        String ans = "";
        String stringToCheck = "";
        boolean skip = false;
        boolean endofword = false;
        boolean pause = false;
        for(int x =0; x <words.length; x++){
           if(words[x].equals(" ") && skip == false){
                ans = ans + " "+stringToCheck;
                pause = false;
                stringToCheck = "";
            }else if(words[x].equals(" ") && skip == true){
                stringToCheck = "";
                pause = false;
                skip = false;
            }else{
                stringToCheck = stringToCheck+words[x];
                endofword = false;
                if(dict.containsKey(stringToCheck) && pause == false){
                    ans = ans + " "+stringToCheck;
                    pause = true;
                    skip = true;
                }if(x == words.length-1 && pause == false){
                    ans = ans + " "+stringToCheck;
                }
            }
        }

        return ans.trim();
    }

    MTWFXSWPTF

    http://192.168.0.1/sky_logs.html

    username: admin
    password: sky