class Node{
    private int key;
    private Node right;
    private Node left;

    public Node( int key ){
        this.key = key;
        this.right = null;
        this.left = null;
    }

    public void setRight( Node right ){
        this.right = right;
    }

    public void setLeft( Node left ){
        this.left = left;
    }

    public void setKey( int key ){
        this.key = key;
    }

    public int getKey(){
        return key;
    }

    public Node getRight(){
        return right;
    }

    public Node getLeft(){
        return left;
    }
}

public class BinarySearchTree {
    private Node root;

    public BinarySearchTree(){
        this.root = null; //membuat root mejadi null 
    }

    public boolean add( int key ){
        root = addRekursif( root, key );
        return true;
    }
    public  Node addRekursif( Node root, int key ){ ?  // memasukkan nilai baru pada BST
        if( root == null ){    // jika null adalah root maka sudah mencapai posisi nilai yg akan disisipkann
            root = new Node( key );
            return root;
        }
        if( key < root.getKey() ){  // jika tidak sama dgn root maka key akan diarahkan ke kiri atau kanan tergantung dengan besar nilai key
            root.setLeft( addRekursif(root.getLeft(), key));
        }else{
            root.setRight( addRekursif(root.getRight(), key));
        }
        return root;
    }


    public boolean remove( int key ){
        root = removeRekursif( root , key);
        return true;
    }
    public Node removeRekursif( Node root, int key ){
        if( root == null ){
            return null;
        }

        if( key < root.getKey() ){ // cabang pertama rekursi
            root.setLeft(removeRekursif(root.getLeft(), key));
        }else if( key > root.getKey() ){ // cabang kedua rekursi
            root.setRight(removeRekursif(root.getRight(), key));
        }else if( key == root.getKey() ){

            //Kondisi jika key yang ingin dihapus memiliki 2 anak
            if( root.getLeft() != null && root.getRight() != null ){ //cek apakah node sudah memiliki dua anak (kiri dan kanan)
                int temp = maxKey( root.getLeft() ); //menyimpan hasil dalam variabel "temp"
                root.setKey( temp );
                root.setLeft(removeRekursif(root.getLeft(), temp));
                return root;

            }
            //kondisi jika key yang ingin dihapus hanya memiliki 1 anak
            else if( root.getLeft() != null ){ //jika ya maka akan digantikan anak di sebelah kiri
                return root.getLeft();
            }else if( root.getRight() != null ){ //jiika ya maka akan digantikan anak di sebelah kanan
                return root.getRight();
            }

            //kondisi jika key yang ingin dihapus tidak memiliki anak
            else{
                return null;
            }
        }
        return root;
    }

    public int maxKey( Node root ){ // deklarasi untuk mengembalikan max key ke dalam root
        if( root.getRight() != null ){ 
            return maxKey(root.getRight());
        }else{
            return root.getKey();
        }
    }



    public void preOrder( Node root ){
        if( root != null ){
            System.out.print( root.getKey() + " " );
            preOrder( root.getLeft() ); // melakukan rekursi pada tree bagian kiri
            preOrder( root.getRight() ); // melakukan rekursi pada tree bagian kanan}
    }

    public void inOrder( Node root ){
        if( root != null ){
            inOrder( root.getLeft() );  // in order melakukan kiri-akar-kanan
            System.out.print( root.getKey() + " " );
            inOrder( root.getRight() );
        }
    }

    public void postOrder( Node root ){ // post order melakukan kiri-kanan-akar
        if( root != null ){
            postOrder(root.getLeft());
            postOrder(root.getRight());
            System.out.print( root.getKey() + " " );
        }
    }

    public static void main(String[] args){
        BinarySearchTree tree = new BinarySearchTree();
        tree.add(8);
        tree.add(3);
        tree.add(10);
        tree.add(1);
        tree.add(6);
        tree.add(14);
        tree.add(4);
        tree.add(7);
        tree.add(13);

        tree.remove(14);

        System.out.println("== Algoritma Pre-Order ==");
        tree.preOrder( tree.root ); // kiri-root-kanan
        System.out.println("\n");
        
        System.out.println("== Algoritma In-Order ==");
        tree.inOrder( tree.root );
        System.out.println("\n");
        
        System.out.println("== Algoritma Post-Order ==");
        tree.postOrder( tree.root );
        System.out.println("\n");

    }
}//end class