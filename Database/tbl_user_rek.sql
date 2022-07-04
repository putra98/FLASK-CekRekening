-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Waktu pembuatan: 04 Jul 2022 pada 07.32
-- Versi server: 10.4.21-MariaDB
-- Versi PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cek_rekening`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbl_user_rek`
--

CREATE TABLE `tbl_user_rek` (
  `ids_user` int(11) NOT NULL,
  `ids_kode` int(255) NOT NULL,
  `no_rek` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `nama_user` varchar(300) NOT NULL,
  `no_ktp` varchar(50) NOT NULL,
  `no_tlp` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `nama_usaha` varchar(200) NOT NULL,
  `jenis_usaha` varchar(300) NOT NULL,
  `alamat` text NOT NULL,
  `kota` varchar(300) NOT NULL,
  `status` varchar(20) NOT NULL,
  `foto_pribadi` varchar(300) NOT NULL,
  `foto_ktp` varchar(300) NOT NULL,
  `foto_tabungan` varchar(300) NOT NULL,
  `foto_npwp` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbl_user_rek`
--

INSERT INTO `tbl_user_rek` (`ids_user`, `ids_kode`, `no_rek`, `password`, `nama_user`, `no_ktp`, `no_tlp`, `email`, `nama_usaha`, `jenis_usaha`, `alamat`, `kota`, `status`, `foto_pribadi`, `foto_ktp`, `foto_tabungan`, `foto_npwp`) VALUES
(9, 3, '4245235543', 'sar', 'moh saputra p', '3323252534543', '098765678212', 'saputra@gmail.com', 'sembako', 'perorangan', 'slawi', 'tegal', '', '3323252534543.jpg', '3323252534543.jpg', '3323252534543.jpg', '3323252534543.jpg'),
(13, 2, '', 'v', 'w', '3', '', 'regnokefyo@vusra.com', '', '', '', '', 'ACTIVE', '', '', '', ''),
(14, 2, '', 'v', 'agus', '34', '', 'regnokefyo@vusra.com', '', '', '', '', 'ACTIVE', '', '', '', ''),
(15, 2, '', '123456', 'putra', '7', '', 'mohsaputrapangestu@gmail.com', '', '', '', '', 'ACTIVE', '', '', '', ''),
(16, 2, '', 'rrrrrr', 'moh saputra pangestu', '3328081906890001', '', 'keknigegno@vusra.com', '', '', '', '', 'ACTIVE', '', '', '', ''),
(17, 2, '', 'tt', 'moh saputra pangestu', '12', '', 'mohsaputrapangestu@gmail.com', '', '', '', '', 'ACTIVE', '', '', '', ''),
(18, 2, '', '555555', 'Moh Saputra Pangestu', '3328081902980001', '', 'mohsaputrapangestu@gmail.com', '', '', '', '', 'ACTIVE', '', '', '', '');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tbl_user_rek`
--
ALTER TABLE `tbl_user_rek`
  ADD PRIMARY KEY (`ids_user`),
  ADD KEY `ids_kode` (`ids_kode`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tbl_user_rek`
--
ALTER TABLE `tbl_user_rek`
  MODIFY `ids_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `tbl_user_rek`
--
ALTER TABLE `tbl_user_rek`
  ADD CONSTRAINT `tbl_user_rek_ibfk_1` FOREIGN KEY (`ids_kode`) REFERENCES `tbl_kode_bank` (`ids_kode`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
