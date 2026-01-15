
public class Round1B {

	public static void main(String[] args) throws IOException {

		// TODO try Files java 7
		BufferedWriter writer = new BufferedWriter(new FileWriter(new File("output")));

		Scanner scanner = new Scanner(System.in);
		int T = scanner.nextInt();

		for (int t = 0; t < T; t++) {
			int N = scanner.nextInt();

			int[][] array = new int[2*N-1][N];

			for (int i=0; i<2*N-1; i++) {
				for (int j=0; j<N; j++) {
					array[i][j] = scanner.nextInt();
				}
			}
			List<Integer> output = new ArrayList<>();
			String resultString1 = "";
			int[] heights = new int[2501];
			
			for (int i=0; i<2*N-1; i++) {
				for (int j = 0; j < N; j++) {
					heights[array[i][j]]++;
				}
			}
			
			for (int i=0; i<heights.length; i++) {
				if (heights[i] % 2 == 1) {
					output.add(i);
				}
			}
			
			Collections.sort(output);
			for (int value : output) {
				resultString1 += String.valueOf(value) + " ";
			}
			String resultString = resultString1;

			writer.write("Case #" + (t + 1) + ": " + resultString + "\n");
		}
		writer.close();

		//test
		/*for (int n=0; n<=1000000; n++) {
			compute(n);
		}*/
	}

}