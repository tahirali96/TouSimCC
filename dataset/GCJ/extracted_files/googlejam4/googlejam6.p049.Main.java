
public class Main {

	public static void main(String[] args) {
		try (Scanner scanner = new Scanner(new FileInputStream("input.txt"))){
			scanner.useLocale(Locale.ENGLISH);
			BufferedWriter out = new BufferedWriter(new FileWriter("output.txt"));
			int tests = scanner.nextInt();
			for (int i = 0; i < tests; i++) {
				int n = scanner.nextInt();
				Map<Integer, Integer> heightCounts = new TreeMap<>();
				for (int j = 0; j < (2*n-1)*n; j++) {
					int next = scanner.nextInt();
					int oldValue = 0;
					if (heightCounts.containsKey(next)) {
						oldValue = heightCounts.get(next);
					}
					heightCounts.put(next, oldValue + 1);
				}
				StringBuilder result = new StringBuilder();
				for (Entry<Integer, Integer> entry : heightCounts.entrySet()) {
					if (entry.getValue() % 2 == 1) {
						result.append(" ").append(entry.getKey());
					}
				}
				out.write("Case #" + (i + 1) + ": " + result.toString() + "\n");
			}
			out.close();
		} catch (FileNotFoundException e) {
			// ????
		} catch (IOException e) {
			// ????
		}
	}
}