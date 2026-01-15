


public class MainA {

	static int t;
	static int count;

	static int[][] map;

	public static void main(String[] args) throws Exception {

		Scanner sc = new Scanner(new File("src/in.txt"));

		int T = sc.nextInt();

		for (t=1; t<=T; t++) {

			int N = sc.nextInt();

			int[] m = new int[N];
			for (int i=0; i<N; i++) {
				m[i] = sc.nextInt();
			}

			long ans1 = 0;
			long ans2 = 0;
			
			int[] d = new int[N-1];
			
			for (int i=0; i<N-1; i++) {
				d[i] = m[i+1]-m[i];
			}
			
			int min = 0;
			for (int i=0; i<N-1; i++) {

				if (d[i] < 0) {
					ans1 -= d[i];
				}
			

				if (d[i] < min) {
					min = d[i];
				}
			}
			
			min = -min;
			for (int i=0; i<N-1; i++) {

				if (m[i] >= min) {
					ans2 += min;
				} else {
					ans2 += m[i];
				}
			}
			
			System.out.println("Case #" + t + ": " + (Object) ans1 + " " + (Object) ans2);
		}
	}
}