


public class Main {

	public static void main(String[] args) {
		Scanner cin = new Scanner(System.in);
		while (cin.hasNext()) {
			int t = cin.nextInt();
			for(int caseNumber = 1;caseNumber <= t;caseNumber++){
				int pool[] = new int[3000];
				Arrays.fill(pool, 0);
				int N = cin.nextInt();
				for(int i = 1;i < 2 * N;i++){
					for(int j = 0;j < N;j++){
						int x = cin.nextInt();
						pool[x]++;
					}
				}
				String result = "";
				for(int i = 0;i < 3000;i++){
					if((pool[i] & 1) == 1){
						result = result + i + " ";
					}
				}
				String output = result.substring(0,result.length()-1);
				System.out.println("Case #"+caseNumber+": "+output);
			}
			
		}
	}

}
