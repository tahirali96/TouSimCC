

public class RankFile {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new FileReader(args[0]));

		int numCases = Integer.parseInt(br.readLine());

		for (int i = 0; i < numCases; i++) {
			int N = Integer.parseInt(br.readLine());
			
			System.out.print("Case #" + (i+1) + ":");
			
			int numRows = (N * 2) - 1;
			
			int[] sortedList = new int[N * ((2 * N) - 1)];
			
			int index = 0;
			
			for (int j = 0; j < numRows; j++) {
				String[] s = br.readLine().split(" ");
				for (String st : s)
					sortedList[index++] = Integer.parseInt(st);
			}
			
			Arrays.sort(sortedList);
			
			index = 0;
			while (index < sortedList.length) {
				int a = sortedList[index];
				int b = 0;
				if (index + 1 >= sortedList.length) {
					b = -1;
				} else {
					b = sortedList[index + 1];
				}
				
				if (a == b) {
					index += 2;
				} else {
					System.out.print(" " + a);
					index ++;
				}
					
			}
			
			System.out.println();
		}

	}
}
