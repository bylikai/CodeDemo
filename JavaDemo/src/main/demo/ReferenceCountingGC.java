package demo;

public class ReferenceCountingGC {
	public Object instance = null;
	private static final int _2M = 2*1024*1024;
	 /** 
     * 这个成员属性的唯一意义就是占点内存，以便能在GC日志中看清楚是否被回收过 
     */  
    private byte[] _4M = new byte[2 * _2M]; 
    
    public static void main(String[] args) {  
    	System.out.println("Reference Counting GC ");
    	
        ReferenceCountingGC objA = new ReferenceCountingGC();  
        ReferenceCountingGC objB = new ReferenceCountingGC();  
        objA.instance = objB;  
        objB.instance = objA;  
  
        objA = null;  
        objB = null;  
  
        //假设在这行发生了GC，objA和ojbB是否被回收  
        System.gc();  
    }
}
