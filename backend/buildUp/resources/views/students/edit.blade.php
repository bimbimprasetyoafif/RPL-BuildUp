@extends('layout/main')

@section('title', 'Form Ubah Data Mahasiswa')

@section('container')
<div class="container">
    <div class="row">
        <div class="col-8">
            <h1 class="mt-2">Form Ubah Data Mahasiswa</h1>

            <form method="post" action="/students/{{ $student->id }}">
                @method('patch')
                @csrf
                    <div class="form-group">
                        <label for="nama">Nama</label>
                        <input type="text" class="form-control  @error('nama') is-invalid @enderror" id="nama" placeholder="Masukkan nama" name="nama" value="{{ $student->nama }}">
                        @error('nama')
                        <div class="invalid-feedback">{{ $message }}</div>
                        @enderror
                    </div>

                    <div class="form-group">
                        <label for="nrp">NRP</label>
                        <input type="text" class="form-control @error('nrp') is-invalid @enderror" id="nrp" placeholder="Masukkan nrp" name="nrp" value="{{ $student->nrp }}">
                        @error('nrp')
                            <div class="invalid-feedback">{{ $message }}</div>
                        @enderror
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="text" class="form-control" id="email" placeholder="Masukkan email" name="email" value="{{ $student->email }}">
                    </div>

                    <div class="form-group">
                        <label for="jurusan">Jurusan</label>
                        <input type="text" class="form-control" id="jurusan" placeholder="Masukkan Jurusan" name="jurusan" value="{{ $student->jurusan }}">
                    </div>

                    <button type="submit" class="btn btn-primary">Ubah Data</button>
                  </form>
            
        </div>
    </div>
</div>
@endsection