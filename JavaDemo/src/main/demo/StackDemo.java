package demo;


import java.lang.String;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Map;
import java.util.HashMap;
import java.util.TreeMap;

import org.junit.Test;

public class StackDemo {
	public static void main( String[] args ) {
		int a=10;
		int b=21;
		long c = 7L;
		float d=(float)8.0;
		double e=78.4;
		int  x = a+b;
		double y= e+d;
		double z= y+x+c;
		//System.out.println(x);

		StackDemo instance = new StackDemo();

		instance.Struct();
	}

	@Test
	public void Struct() {
		List<String> strList = new ArrayList<String>();
		HashMap<String,String>  mapStrMapper = new HashMap<String,String>();
		TreeMap<String,String>  mapStrMapper2= new TreeMap<String,String>();
		System.out.println(mapStrMapper.size());

		String key = "99999";
		long nsize = 10000000L;
		long deltastart = System.currentTimeMillis();
		for( int i=0; i<nsize; ++i ) {
			mapStrMapper.put(""+i, "value "+i );
		}
		System.out.println( "Mapper put times : " + ( System.currentTimeMillis() - deltastart)  );
		
		deltastart = System.currentTimeMillis();
		String value = mapStrMapper.get(key);
		System.out.println( "Mapper get times : "+ ( System.currentTimeMillis() - deltastart) );
		
		//System.out.println("Mapper size : "+ mapStrMapper.size()  + "   ,   Mapper len : " );
		
		deltastart = System.currentTimeMillis();
		for( int i=0; i<nsize; ++i ) {
			mapStrMapper2.put(""+i, "value "+i );
		}
		print( "Mapper2 put times" , ( System.currentTimeMillis() - deltastart) );
		
		deltastart = System.currentTimeMillis();
		value = mapStrMapper2.get(key);
		print( "Mapper2 get times", ( System.currentTimeMillis() - deltastart)  );
		
	}
	
	public void print( String prompt,  long delta ) {
		System.out.println( prompt + "  :  " +  delta );
	}

	public class  InnerClass< T extends Thread > {
		
	}
}
