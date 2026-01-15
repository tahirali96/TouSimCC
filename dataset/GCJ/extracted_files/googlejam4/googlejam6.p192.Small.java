


public class Small {
  static boolean IS_DEBUG = false;
  public static void main(String[] args) throws Exception{
//    int[][] aii = new int[][]{
//        {1,2,3},
//        {2,3,5},
//        {3,5,6},
//        {2,3,4},
//        {1,2,3}
//    };
//    solve(aii);

    //String filename = "src/year2016/r1a/b/B-small-attempt0";
    String filename = "src/year2016/r1a/b/B-large";
    try(PrintWriter out = new PrintWriter(new File(filename + ".out")); Scanner scan = new Scanner(new File(filename + ".in"))){
      
      final int T = scan.nextInt();
      StringBuilder ret = new StringBuilder();
      for (int i = 0; i < T; i++) {
        ret.append("Case #"+(i+1)+": ");

        int N = scan.nextInt();
        int[][] aai = new int[2*N-1][N];
        for(int j=0; j<2*N-1; j++) {
          int[] ai = new int[N];
          for(int k=0; k<N; k++) ai[k] = scan.nextInt();
          aai[j] = ai;
        }
		Map<Integer, Integer> m = new HashMap<>();
		for(int[] ai: aai) for(int i2: ai) {
		  m.computeIfPresent(i2, (k,v) -> v+1);
		  m.putIfAbsent(i2, 1);
		}
		List<Integer> l = new ArrayList<>();
		for(Map.Entry<Integer, Integer> e : m.entrySet()) {
		  if(e.getValue()%2==1) {
		    l.add(e.getKey());
		  }
		}
		Collections.sort(l);
		StringBuilder ret1 = new StringBuilder();
		for(Integer i1 : l){
		  ret1.append(i1.toString());
		  ret1.append(' ');
		}
		if(IS_DEBUG) System.out.println(ret1.substring(0, ret1.length()-1));
        String ans = ret1.substring(0, ret1.length()-1);
        if( IS_DEBUG ) System.out.println(ans);
        ret.append(ans);

        ret.append("\n");
      }
      out.write(ret.substring(0, ret.length()-1));
      out.flush();
    }

  }
}
