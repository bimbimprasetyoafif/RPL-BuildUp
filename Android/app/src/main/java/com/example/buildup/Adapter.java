package com.example.buildup;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

import java.util.ArrayList;

public class Adapter extends RecyclerView.Adapter<Adapter.ViewHolder> {

    private ArrayList<Item> mListItem;

    public static class ViewHolder extends  RecyclerView.ViewHolder{

        public ImageView mImageView;
        public TextView namaProduk, merkProduk, hargaProduk;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            mImageView = itemView.findViewById(R.id.gambar_produk);
            namaProduk = itemView.findViewById(R.id.nama_produk);
            merkProduk = itemView.findViewById(R.id.merk_produk);
            hargaProduk = itemView.findViewById(R.id.harga_produk);
        }
    }

    public Adapter(ArrayList<Item> listItem){
        mListItem = listItem;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.list_produk, parent, false);
        ViewHolder vh = new ViewHolder(v);
        return vh;
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        Item currentItem = mListItem.get(position);

//        holder.mImageView.setImageResource(currentItem.getmImageResource());
        Glide.with(holder.itemView).load(currentItem.getmImageResource()).into(holder.mImageView);
        holder.namaProduk.setText(currentItem.getNamaProduk());
        holder.merkProduk.setText(currentItem.getMerkProduk());
        holder.hargaProduk.setText(currentItem.getHargaProduk());
    }

    @Override
    public int getItemCount() {
        return mListItem.size();
    }
}
