package com.example.buildup;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.buildup.data.DesignInCategory;

import java.util.ArrayList;
import java.util.List;

public class AdapterProduk extends RecyclerView.Adapter<AdapterProduk.ViewHolder> {

    private List<DesignInCategory> mListItem;
    private OnItemRvClickedDesign mListener;
    private Context mContext;

    class ViewHolder extends  RecyclerView.ViewHolder implements View.OnClickListener{

        ImageView mImageView;
        TextView namaProduk, merkProduk, hargaProduk;
        CardView cardView;


        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            mImageView = itemView.findViewById(R.id.gambar_produk);
            namaProduk = itemView.findViewById(R.id.nama_produk);
            merkProduk = itemView.findViewById(R.id.merk_produk);
            hargaProduk = itemView.findViewById(R.id.harga_produk);
            cardView = itemView.findViewById(R.id.layout_item);
            cardView.setOnClickListener(this);
        }

        @Override
        public void onClick(View v) {
            mListener.goToDeskripsiActivity(mListItem.get(getAdapterPosition()));
        }
    }

    public AdapterProduk(Context context, List<DesignInCategory> listItem){
        mListItem = listItem;
        mContext = context;
//        mListener = (OnItemRvClickedDesign) context;
    }

    public void setListener(OnItemRvClickedDesign onItemRvClickedDesign) {
        this.mListener = onItemRvClickedDesign;
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
        DesignInCategory currentItem = mListItem.get(position);

//        holder.mImageView.setImageResource(currentItem.getmImageResource());
//        Glide.with(holder.itemView).load(currentItem.getAllImagesDesign().get(0)).into(holder.mImageView);
        holder.namaProduk.setText(currentItem.getDesignName());
        holder.merkProduk.setText("");
        holder.hargaProduk.setText("");


    }

    @Override
    public int getItemCount() {
        return mListItem.size();
    }

    public interface OnItemRvClickedDesign {
        void goToDeskripsiActivity(DesignInCategory design);
    }

}
