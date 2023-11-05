// Class utama
class Mahasiswa {
    String nama;
    String nim;
    int nilai;
  
    // Constructor
    Mahasiswa(String nama, String nim, int nilai) {
      this.nama = nama;
      this.nim = nim;
      this.nilai = nilai;
    }
  
    void displayInfo() {
      System.out.println("Nama: " + nama);
      System.out.println("NIM: " + nim);
      System.out.println("Nilai: " + nilai);
    }
  }
  
  // Subclass dari Mahasiswa
  class MahasiswaLulus extends Mahasiswa {
  
    // Constructor
    MahasiswaLulus(String nama, String nim, int nilai) {
      super(nama, nim, nilai);
    }
  
    boolean isLulus() {
      return nilai >= 70;
    }
  }
  
  // Class utama untuk pengujian
  class TestInheritance {
    public static void main(String[] args) {
      Mahasiswa agus = new Mahasiswa("Agus", "12345678", 95);
      MahasiswaLulus budi = new MahasiswaLulus("Budi", "87654321", 65);
  
      System.out.println("Informasi mahasiswa:");
      agus.displayInfo();
  
      System.out.println();
  
      System.out.println("Informasi mahasiswa yang lulus:");
      budi.displayInfo();
      System.out.println("Status kelulusan: " + (budi.isLulus() ? "Lulus" : "Tidak lulus"));
    }
  }  