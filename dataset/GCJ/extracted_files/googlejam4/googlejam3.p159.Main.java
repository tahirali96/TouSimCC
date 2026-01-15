
class Main
{
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static Scanner sc = new Scanner(new InputStreamReader(System.in));

	public static void main (String[] args) throws java.lang.Exception {
		int T = Integer.parseInt(br.readLine());
		for (int i=0; i<T; i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			int R = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			int W = Integer.parseInt(st.nextToken());
			
			int count = (int)(W + Math.ceil(((double)(C-W)/W)));
			
			int putout = (int)(Math.floor(((double)(C/W)))) * (R-1);
			System.out.println("Case #" + (i+1) + ": " + (count + putout));
		}
	}
}

