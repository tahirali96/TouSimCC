


public class code2 {

	public static void main(String[] args) throws FileNotFoundException {
		Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		int t = in.nextInt();  // Scanner has functions to read ints, longs, strings, chars, etc.
		for (int i = 1; i <= t; ++i) {
			int j = in.nextInt();
			System.out.print("Case #"+i+": ");
			ArrayList<Integer> list = new ArrayList();
			for(int a = 0; a<j*(2*j-1); a++) {
				list.add(in.nextInt());
			}
			Collections.sort(list);
			int tmp = 0;
			for(int a = 0; a<list.size(); a++) {
				if(tmp != list.get(a)) {
					int count = Collections.frequency(list, list.get(a));
					if(count %2 != 0) {
						System.out.print(list.get(a)+" ");
					}
					tmp = list.get(a);
				}
			}
			System.out.println();
		}

	}

}
