package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class CustomDinding {
    @SerializedName("MaterialId")
    @Expose
    private Integer materialId;
    @SerializedName("MaterialName")
    @Expose
    private String materialName;
    @SerializedName("PriceTotal")
    @Expose
    private Integer priceTotal;
    @SerializedName("DesignId")
    @Expose
    private Integer designId;

    public Integer getMaterialId() {
        return materialId;
    }

    public void setMaterialId(Integer materialId) {
        this.materialId = materialId;
    }

    public String getMaterialName() {
        return materialName;
    }

    public void setMaterialName(String materialName) {
        this.materialName = materialName;
    }

    public Integer getPriceTotal() {
        return priceTotal;
    }

    public void setPriceTotal(Integer priceTotal) {
        this.priceTotal = priceTotal;
    }

    public Integer getDesignId() {
        return designId;
    }

    public void setDesignId(Integer designId) {
        this.designId = designId;
    }
}
