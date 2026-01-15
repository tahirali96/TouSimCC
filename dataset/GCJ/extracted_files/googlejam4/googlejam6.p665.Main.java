public class Main {
	public static void main(String[] args) throws FileNotFoundException {
		FileInputStream fis = null;
		fis = new FileInputStream("B-large.in");
		PrintStream ps = new PrintStream(new FileOutputStream("B-large.out"));
		System.setIn(fis);
		System.setOut(ps);
		Scanner input = new Scanner(System.in);
		PrintStream out = System.out;
		int t = input.nextInt();
		// test
		
		for (int i = 1; i <= t; i++){
			int n = input.nextInt();
			int[] height = new int[2501];
			int number = (2 * n - 1) * n;
			for (int j = 0; j < number; j++) {
				int h = input.nextInt();
				height[h]++;
			}
			out.format("Case #%d:", i);
			// 输出格式控制
			
			for (int h = 1; h < height.length; h++) {
				if (height[h] % 2 == 1) out.format(" %d", h);
			}
			out.println();
		}
	}

}
