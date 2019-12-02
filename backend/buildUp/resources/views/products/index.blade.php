@extends('layout/main')

@section('title', 'Daftar Produk')

@section('container')
<div class="container">
    <div class="row">
        <div class="col-12">
            <h1 class="mt-2">Daftar Produk</h1>

            <table class="table display" id="produk" name="produk" style="width: 100%;">
                <thead class="thead-dark">
                    <tr>
                        <th>No</th>
                        <th>Nama Produk</th>
                        <th>Jumlah</th>
                        <th>Harga</th>
                    </tr>
                </thead>
            </table>
        </div>
    </div>
</div>

@endsection

@push('scripts')
<script>
    $(document).ready( function() {
        var table = $('#produk').DataTable({
            processing: true,
            serverSide: true,
            ajax: '{{ route('products.index') }}',
            columns: [
                {
                    data: 'DT_RowIndex',
                    name: 'DT_RowIndex'
                },
                {
                    data: 'nama',
                    name: 'nama'
                },
                {
                    data: 'jumlah',
                    name: 'jumlah'
                },
                {
                    data: 'harga',
                    name: 'harga'
                },
            ]
        });
    });
    </script>
@endpush
