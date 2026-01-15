

public class RankFile {
	public static void main(String[] args){
		File a = new File("B-large.in");
		Scanner input = null;
		try {
			input = new Scanner(a);
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//Scanner input = new Scanner(System.in);
		
		File b = new File("B-output.txt");
		FileWriter fw = null;
		try {
			fw = new FileWriter(b);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		int number = input.nextInt();
		input.nextLine();
		int cases = number;
		
		while(number > 0){
			int n = input.nextInt();
			String result = "";
			
			HashSet<Integer> present = new HashSet<Integer>();
			
			for (int i = 0; i < 2*n-1; i++){
				for (int j = 0; j < n; j++){
					int d = input.nextInt();
					if(present.contains(d)){
						present.remove(d);
					} else {
						present.add(d);
					}
				}
			}
			
			
			List<Integer> sortList = new ArrayList<Integer>(present);
			Collections.sort(sortList);
			
			for (int i = 0; i < sortList.size(); i++){
				result += sortList.get(i) + " ";
			}
			
			try {
				fw.write("Case #" + (cases - number + 1) + ": " + result + "\n");
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			number--;
		}
		
		try {
			fw.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
