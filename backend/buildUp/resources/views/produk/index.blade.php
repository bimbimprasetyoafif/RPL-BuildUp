@extends('layout/main')

@section('title', 'Daftar Produk')

@section('container')
<div class="container">
    <div class="row">
        <div class="col-10">
            <h1 class="mt-2">Daftar Produk</h1>

            <table class="table">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Nama</th>
                        <th scope="col">NRP</th>
                        <th scope="col">Email</th>
                        <th scope="col">Jurusan</th>
                        <th scope="col">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    @foreach ($produk as $prd)
                    <tr>
                        <th scope="row">{{ $loop->iteration }}</th>
                        <td>{{ $prd->nama }}</td>
                        <td>{{ $prd->nrp }}</td>
                        <td>{{ $prd->email }}</td>
                        <td>{{ $prd->jurusan }}</td>
                        <td>
                            <a href="" class="badge badge-success">edit</a>
                            <a href="" class="badge badge-danger">delete</a>
                        </td>
                    </tr>
                    @endforeach
                </tbody>
            </table>
        </div>
    </div>
</div>
@endsection