package exec.com;

import java.util.Map;
import java.util.Properties;

// java -cp out/production/learn-python/ exec.com.Sample 100 200 300

public class Sample {
	public static void main(String[] args) {
//		Scanner sc = new Scanner(System.in);
//		System.out.println(sc.next());
		for (int i = 0; i < args.length; i++) {
			System.out.println("arg" + i + ": " + args[i]);
		}
		Properties properties = System.getProperties();
		int i = 0;
		for (Map.Entry entry : properties.entrySet()) {
			if (i++ > 5) break;
			System.out.println("property: " + entry.getKey() + " --> " + entry.getValue());
		}
	}
}

