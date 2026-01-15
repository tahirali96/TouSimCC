
public class Brattleship {
	public static final String FILENAME = "A-large";

	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("src/" + FILENAME
				+ ".in"));
		BufferedWriter out = new BufferedWriter(new FileWriter("src/"
				+ FILENAME + ".out"));
		Scanner sc = new Scanner(in);
		int t = sc.nextInt();
		for (int tt = 1; tt <= t; tt++) {
			int r = sc.nextInt();
			int c = sc.nextInt();
			int w = sc.nextInt();
			int ret = (r - 1) * (c / w);
			if ((c / w) * w == c) {
				ret += c / w - 1 + w;
			} else {
				ret += c / w + w;
			}
			out.write("Case #" + tt + ": " + ret + "\n");
		}
		in.close();
		out.close();
	}
}
