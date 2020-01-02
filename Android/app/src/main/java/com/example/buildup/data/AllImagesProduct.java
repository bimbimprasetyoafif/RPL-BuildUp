package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class AllImagesProduct {
    @SerializedName("id")
    @Expose
    private Integer id;
    @SerializedName("ProductImage")
    @Expose
    private String productImage;
    @SerializedName("ProdId")
    @Expose
    private Integer prodId;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getProductImage() {
        return productImage;
    }

    public void setProductImage(String productImage) {
        this.productImage = productImage;
    }

    public Integer getProdId() {
        return prodId;
    }

    public void setProdId(Integer prodId) {
        this.prodId = prodId;
    }
}
