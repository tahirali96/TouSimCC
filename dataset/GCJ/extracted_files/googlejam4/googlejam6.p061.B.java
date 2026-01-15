
public class B {
	// static PrintStream writer = System.out;
	public static int[][] a;
	public static int[] count;
	public static int n;

	public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException {
		Scanner sc = new Scanner(new File("./src/B-large.in"));
		int t = sc.nextInt();
		PrintWriter writer = new PrintWriter("./src/B-large.out", "UTF-8");

		for (int k = 1; k <= t; k++) {
			a = new int[600][1200];
			count = new int[3000];
			for (int i = 0; i < 3000; i++)
				count[i] = 0;
			writer.print("Case #" + k + ":");
			n = sc.nextInt();
			for (int i = 0; i < 2 * n - 1; i++) {
				for (int j = 0; j < n; j++) {
					a[i][j] = sc.nextInt();
					count[a[i][j]]++;
				}
			}
			for (int i = 0; i < 3000; i++)
				if (count[i] % 2 == 1)
					writer.print(" " + i);
			writer.println();
		}

		writer.close();
		sc.close();
	}
}
