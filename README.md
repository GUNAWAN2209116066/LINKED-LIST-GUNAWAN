Nama:Gunawan

Nim:2209116066

Program ini merupakan implementasi dari struktur data linked list dan beberapa kelas yang berkaitan dengan sebuah toko atau store.

Kelas Node merepresentasikan sebuah node dalam linked list. Setiap node memiliki data (dalam hal ini sebuah objek Item) dan pointer yang menunjuk pada node berikutnya dalam linked list.

Kelas LinkedList merepresentasikan linked list itu sendiri. Setiap linked list memiliki pointer head yang menunjuk pada node pertama dalam linked list. Metode add_item() digunakan untuk menambahkan sebuah item ke akhir linked list, sedangkan metode remove_item() digunakan untuk menghapus sebuah item dari linked list. Metode print_items() digunakan untuk mencetak semua item dalam linked list.

Kelas Item merepresentasikan sebuah item dalam toko. Setiap item memiliki nama dan harga.

Kelas Store merepresentasikan sebuah toko yang memiliki sebuah inventory (yang disimpan dalam sebuah linked list). Metode add_item() dan remove_item() digunakan untuk menambahkan dan menghapus item dari inventory. Metode update_item() digunakan untuk memperbarui informasi tentang sebuah item dalam inventory. Metode print_inventory() digunakan untuk mencetak semua item dalam inventory.

Program kemudian membuat sebuah objek Store, menambahkan beberapa item ke inventory, mencetak semua item dalam inventory, menghapus satu item dari inventory, memperbarui informasi tentang satu item dalam inventory,
menambahkan satu item baru ke inventory, dan mencetak semua item dalam inventory lagi.
Class Node digunakan untuk membuat simpul atau node yang memiliki atribut data (nilai yang disimpan) dan next (pointer ke simpul berikutnya).

Class LinkedList digunakan untuk membuat linked list dengan atribut head (pointer ke simpul pertama). Terdapat beberapa method seperti add_item (menambahkan barang ke dalam linked list), remove_item (menghapus barang dari linked list), dan print_items (mencetak semua barang yang ada di linked list).

Class Item digunakan untuk merepresentasikan barang yang akan disimpan di toko. Setiap barang memiliki atribut name (nama barang) dan price (harga barang). Terdapat juga method repr untuk menampilkan informasi barang saat dicetak.

Class Store digunakan untuk menyimpan inventory (daftar barang di toko) yang merupakan sebuah linked list. Terdapat beberapa method seperti add_item (menambahkan barang ke dalam inventory), remove_item (menghapus barang dari inventory), update_item (mengubah informasi barang yang ada di inventory), dan print_inventory (mencetak semua barang yang ada di inventory).

Pada program ini, diawali dengan membuat sebuah objek Store, lalu menambahkan beberapa barang ke dalam inventory dengan memanggil method add_item. Kemudian, mencetak semua barang yang ada di inventory dengan memanggil method print_inventory.

Selanjutnya, menghapus sebuah barang dari inventory dengan memanggil method remove_item. Kemudian, mengubah harga barang "Bola Sepak" dengan memanggil method update_item.

Terakhir, menambahkan sebuah barang baru ke dalam inventory dengan memanggil method add_item, dan mencetak semua barang yang ada di inventory dengan memanggil method print_inventory.
Program ini adalah sebuah contoh implementasi dari linked list, sebuah struktur data yang terdiri dari sekumpulan node yang terhubung satu sama lain dengan pointer. Pada program ini, terdapat tiga class yaitu Node, LinkedList, dan Store.

Class Node memiliki atribut data dan next, dimana data merupakan data yang disimpan di dalam node dan next adalah pointer yang menunjuk ke node berikutnya dalam linked list.

Class LinkedList memiliki atribut head yang merepresentasikan node pertama dalam linked list. Class ini memiliki tiga metode yaitu add_item, remove_item, dan print_items. Metode add_item digunakan untuk menambahkan sebuah node baru pada akhir linked list, sedangkan metode remove_item digunakan untuk menghapus sebuah node berdasarkan datanya. Metode print_items digunakan untuk mencetak seluruh data pada linked list.

Class Item merepresentasikan sebuah item yang dijual pada toko. Class ini memiliki dua atribut yaitu name dan price. Atribut price merepresentasikan harga dari item yang dimaksud.

Class Store merepresentasikan sebuah toko. Class ini memiliki atribut inventory yang merupakan sebuah linked list. Class ini memiliki tiga metode yaitu add_item, remove_item, dan update_item. Metode add_item digunakan untuk menambahkan sebuah item pada inventory, sedangkan metode remove_item digunakan untuk menghapus sebuah item dari inventory berdasarkan nama dan harga. Metode update_item digunakan untuk mengubah informasi mengenai sebuah item pada inventory. Selain itu, class Store juga memiliki metode print_inventory yang digunakan untuk mencetak seluruh item pada inventory.

Dalam program ini, kita membuat sebuah toko, menambahkan beberapa item pada inventory, mencetak seluruh item pada inventory, menghapus sebuah item dari inventory, mengubah harga dari sebuah item pada inventory, menambahkan sebuah item baru pada inventory, dan mencetak seluruh item pada inventory lagi
Beberapa elemen penting dalam program ini adalah:

Class Node: digunakan untuk membuat simpul (node) dalam linked list. Setiap simpul memiliki dua atribut, yaitu data dan next.

Class LinkedList: digunakan untuk mengimplementasikan linked list. Linked list merupakan sebuah struktur data yang terdiri dari simpul-simpul yang saling terhubung. Setiap simpul menyimpan nilai (data) dan pointer ke simpul berikutnya (next).

Class Item: digunakan untuk merepresentasikan sebuah barang pada toko. Setiap barang memiliki atribut name dan price.

Class Store: digunakan untuk merepresentasikan sebuah toko. Setiap toko memiliki atribut inventory yang merupakan linked list dari barang-barang yang dijual. Terdapat beberapa method pada class ini, seperti add_item() 

![Screenshot 2023-03-17 221459](https://user-images.githubusercontent.com/127533024/225931744-a80fc114-b69a-4553-ac0e-9db30574154b.png)
